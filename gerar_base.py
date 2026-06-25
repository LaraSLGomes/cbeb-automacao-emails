import pandas as pd

dados = {
    "Pergunta": [
        # CATEGORIA: INSCRIÇÕES
        "Onde faço minha inscrição?",
        "Qual o valor da inscrição?",
        "Quais documentos preciso para inscrição de estudante?",
        "Posso pagar por Nota de Empenho?",
        "Como me associar à SBEB para ter desconto?",
        "O que a inscrição como ouvinte inclui?",
        # CATEGORIA: SUBMISSÕES
        "Como submeto meu artigo?",
        "Qual template usar?",
        "Quantos artigos posso submeter?",
        "Posso submeter em português?",
        "Ouvinte pode submeter artigo?",
        "Qual o prazo para submissão?",
        "Preciso pagar para submeter?",
        "Outra pessoa pode apresentar meu trabalho?",
        # CATEGORIA: EVENTO E LOGÍSTICA
        "Quando e onde será o CBEB 2026?",
        "Quais as atividades do congresso?",
        "Hotéis e hospedagem?",
        # CATEGORIA: CANCELAMENTO E REEMBOLSO
        "Como cancelo minha inscrição?",
        "Posso transferir para outra pessoa?",
        # CATEGORIA: MINICURSOS E ATIVIDADES
        "Preciso estar inscrito no congresso para fazer minicurso?",
        "Preciso estar inscrito no congresso para o Ideathon?",
        # CATEGORIA: COQUETEL
        "O coquetel é incluído na inscrição?",
        # CATEGORIA: CONTATO
        "Como falo com a organização?"
    ],
    "Resposta": [
        # CATEGORIA: INSCRIÇÕES
        "A inscrição é realizada pela plataforma oficial do CBEB 2026. Basta acessar o link de inscrição no site oficial e seguir as instruções.",
        "Os valores variam por categoria e lote. Profissional: a partir de R$ 550 (sócio) / R$ 650 (não sócio); Graduação: a partir de R$ 250 / R$ 350; Pós-Graduação: a partir de R$ 350 / R$ 450. Lote 1 até 31/05/2026. Confira todos os valores na página de inscrições.",
        "Estudantes de graduação e pós-graduação devem anexar carteirinha estudantil ou declaração de matrícula válida no ato da inscrição.",
        "Sim. Envie e-mail para cbeb2026@sbeb.org.br com assunto 'Solicitação de dados para nota de empenho'.",
        "Acesse o site de associação da SBEB para verificar os benefícios e realizar sua filiação. Como sócio, você terá desconto em todas as categorias de inscrição.",
        "A inscrição de Ouvinte é por diária (R$ 100/dia) e dá acesso a sessões plenárias, palestras, workshops, mesas-redondas e coffee-break. Não permite submissão de artigos.",
        # CATEGORIA: SUBMISSÕES
        "A submissão de artigos é feita exclusivamente pela plataforma oficial. Use o template IEEE e envie em formato PDF.",
        "É obrigatório usar o template IEEE. Recomendamos usar o modelo disponível no Overleaf para facilitar a formatação.",
        "Cada inscrição nas categorias Graduando, Pós-Graduando e Profissional permite a submissão de até 2 artigos.",
        "Sim. Aceita-se artigos em inglês e português. Artigos em inglês com mérito podem ser publicados no IEEE Xplore. Em português, a publicação é via Proceedings SBEB no Zenodo.",
        "Não. As categorias Ouvinte, Minicursos e Ideathon não permitem submissão de artigos. Para submeter, inscreva-se como Graduando, Pós-Graduando ou Profissional.",
        "O prazo para submissão de artigos é até 30 de junho de 2026. A notificação de aceite será até 15 de julho e a versão final até 30 de julho de 2026.",
        "Não. Você pode submeter e aguardar a avaliação. Porém, a publicação nos anais está condicionada ao pagamento da inscrição até 30 de agosto de 2026.",
        "Sim, qualquer autor inscrito no CBEB pode apresentar o trabalho.",
        # CATEGORIA: EVENTO E LOGÍSTICA
        "O CBEB 2026 será realizado de 28 de setembro a 02 de outubro de 2026, na Fábrica de Negócios – Hotel Praia Centro, Av. Monsenhor Tabosa, 740 – Praia de Iracema, Fortaleza/CE.",
        "O CBEB 2026 contará com palestras, plenárias, mesas-redondas, minicursos, apresentações orais e de pôsteres, BioChallenge, Ideathon, Prêmios SBEB e pitchs de startups.",
        "Consulte a página de Hospedagem e Mobilidade no site oficial do CBEB 2026 para informações sobre convênios com hotéis próximos e opções de transporte.",
        # CATEGORIA: CANCELAMENTO E REEMBOLSO
        "Envie e-mail para cbeb2026@sbeb.org.br solicitando o cancelamento. O prazo é de até 30 dias antes do início do evento. Será retido 30% do valor pago a título de taxas administrativas.",
        "Sim. A substituição de participante pode ser solicitada por e-mail até 7 dias antes do início do evento.",
        # CATEGORIA: MINICURSOS E ATIVIDADES
        "Sim. Os minicursos pré-congresso são exclusivos para inscritos no CBEB 2026, com inscrição adicional de R$ 200. Vagas limitedas.",
        "Não. O Ideathon é aberto ao público, inclusive para quem não está inscrito no congresso. Inscrição: R$ 250. Vagas limitadas.",
        # CATEGORIA: COQUETEL
        "Apenas para a categoria Profissional, sujeito à capacidade do local. Para acompanhantes, a taxa é R$ 200 a partir de 15/07. Para demais categorias, ingressos avulsos de R$ 200 poderão ser liberados a partir de 15/08, se houver vagas.",
        # CATEGORIA: CONTATO
        "Você pode entrar em contato por: E-mail: cbeb2026@sbeb.org.br · WhatsApp: (85) 99178-1720 · Para patrocínio: leonardo@emaisassessoria.com.br"
    ]
}

df = pd.DataFrame(dados)
df.to_excel("perguntas_respostas.xlsx", index=False)
print("✔ Planilha 'perguntas_respostas.xlsx' gerada com sucesso e de forma isolada!")