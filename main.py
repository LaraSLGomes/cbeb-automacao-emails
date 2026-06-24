import imaplib
import smtplib
import email
from email.mime.text import MIMEText
import pandas as pd
from openai import OpenAI

# 1. CONFIGURAÇÕES E CREDENCIAIS

IA_API_KEY = "sua_chave_da_api_aqui"

# dados email
EMAIL_USER = "seu_email@institucional.edu.br" 
EMAIL_PASS = "SuaSenhaNormalDeAcesso" 

# servidores padrão 
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"

client = OpenAI(api_key=IA_API_KEY)

# 2. CARREGAR A BASE DE CONHECIMENTO
def carregar_base_conhecimento():
    try:
        # lê o arquivo do excel
        df = pd.read_excel("perguntas_respostas.xlsx")
        contexto = ""
        for _, linha in df.iterrows():
            contexto += f"Pergunta: {linha['Pergunta']}\nResposta: {linha['Resposta']}\n---\n"
        return contexto
    except Exception as e:
        print(f"Erro ao carregar a planilha: {e}")
        return None

# 3. GERAR RESPOSTA COM IA (CONTEXTUALIZADA)
def gerar_resposta_ia(corpo_email, base_conhecimento):
    prompt_sistema = f"""
    Você é um assistente de atendimento automatizado focado em responder e-mails institucionais. 
    Use APENAS a base de conhecimento abaixo para responder ao e-mail do usuário.
    Se a resposta exata ou o contexto não puder ser encontrado na base de conhecimento fornecida, responda estritamente com a palavra: REPASSO_HUMANO.
    
    Regras:
    1. Seja profissional, educado e direto.
    2. Não invente nenhuma informação que não esteja explicitamente na base abaixo.
    
    Base de Conhecimento:
    {base_conhecimento}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # modelo rápido e econômico
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": f"E-mail recebido:\n{corpo_email}"}
        ],
        temperature=0.2  # evitar que a IA invente dados (alucinação)
    )
    return response.choices[0].message.content

# 4. ENVIAR O E-MAIL DE RESPOSTA
def enviar_email(destinatario, assunto, corpo):
    msg = MIMEText(corpo)
    msg['Subject'] = f"Re: {assunto}"
    msg['From'] = EMAIL_USER
    msg['To'] = destinatario

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, destinatario, msg.as_string())
        print(f"-> Resposta enviada com sucesso para: {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

# 5. FLUXO PRINCIPAL
def processar_emails():
    base = carregar_base_conhecimento()
    if not base:
        print("Processo interrompido: Base de conhecimento vazia ou ilegível.")
        return
    
    print("Conectando ao servidor de e-mail...")
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")
    except Exception as e:
        print(f"Erro de autenticação ou conexão no e-mail: {e}")
        print("Verifique se seu e-mail/senha estão corretos ou se o servidor IMAP exige configurações da instituição.")
        return

    # busca por e-mails não lidos (UNSEEN)
    status, mensagens = mail.search(None, 'UNSEEN')
    ids_emails = mensagens[0].split()
    
    if not ids_emails:
        print("Nenhum e-mail novo não lido encontrado.")
        mail.close()
        mail.logout()
        return

    print(f"Encontrado(s) {len(ids_emails)} e-mail(s) para processar.")
    
    for num in ids_emails:
        status, data = mail.fetch(num, '(RFC822)')
        for resposta in data:
            if isinstance(resposta, tuple):
                msg = email.message_from_bytes(resposta[1])
                remetente = email.utils.parseaddr(msg['From'])[1]
                assunto = msg['Subject']
                
                # pula respostas automáticas dele mesmo para evitar loops infinitos
                if remetente == EMAIL_USER:
                    continue
                
                # extrai o corpo do e-mail em formato texto simples
                corpo = ""
                if msg.is_multipart():
                    for parte in msg.walk():
                        if parte.get_content_type() == "text/plain":
                            corpo = parte.get_payload(decode=True).decode(errors='ignore')
                            break
                else:
                    corpo = msg.get_payload(decode=True).decode(errors='ignore')

                print(f"\nProcessando e-mail de: {remetente} | Assunto: {assunto}")
                
                # processamento com IA baseada na Planilha
                resposta_final = gerar_resposta_ia(corpo, base)
                
                if resposta_final.strip() == "REPASSO_HUMANO":
                    print(f"-> IA não encontrou a resposta na planilha. Mantendo como não lido para suporte humano.")
                    # remove a marcação de lido para que você veja na sua caixa normal
                    mail.store(num, '-FLAGS', '\\Seen')
                else:
                    enviar_email(remetente, assunto, resposta_final)
                    # marca permanentemente como lido apenas se respondeu
                    mail.store(num, '+FLAGS', '\\Seen')

    mail.close()
    mail.logout()
    print("\nExecução finalizada.")

if __name__ == "__main__":
    processar_emails()