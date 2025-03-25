from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

# Criando o PDF
doc = SimpleDocTemplate("Curriculo_Enuk.pdf", pagesize=letter)

# Criando o estilo do PDF
styles = getSampleStyleSheet()
normal_style = styles['Normal']
normal_style.fontName = 'Helvetica'
normal_style.fontSize = 12
normal_style.leading = 14  

# Estilo para os títulos
heading_style = ParagraphStyle(
    name='Heading1',
    fontName='Helvetica-Bold',
    fontSize=16,
    spaceAfter=12,
)

# Função para O hyperlink
def add_link(c, x, y, text, url):
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.blue)
    c.linkURL(url, (x, y, x + 200, y + 12))
    c.drawString(x, y, text)

# Conteudo do curriculo
content = []

# Adicionando o nome e contato
content.append(Paragraph('ENUK DOS SANTOS ALVES NOGUEIRA', heading_style))
content.append(Paragraph("Guarulhos, SP | (11) 97073-0434 | enuk.santos@gmail.com", normal_style))
content.append(Spacer(1, 12))

# Adicionando o LinkedIn 
content.append(Paragraph("LinkedIn:", normal_style))
content.append(Spacer(1, 6))  # Pequeno espaçamento
content.append(Paragraph('<link href="https://www.linkedin.com/in/enuk-nogueira">https://www.linkedin.com/in/enuk-nogueira-35769b193/</link>', normal_style))
content.append(Spacer(1, 12))

# Resumo profissional
content.append(Paragraph('RESUMO PROFISSIONAL', heading_style))
content.append(Paragraph(
    "Graduando em Engenharia de Software com experiência em documentação técnica, "
    "gestão de processos e suporte técnico. Possuo conhecimento em linguagens de programação "
    "(Python, C#, Java, JavaScript), redes e protocolos de comunicação e uso de ferramentas como "
    "Jira e Power BI. Busco uma oportunidade para aplicar e expandir meus conhecimentos em TI, "
    "contribuindo para projetos inovadores e eficientes.", normal_style))
content.append(Spacer(1, 12))

# Formação Acadêmica
content.append(Paragraph('FORMAÇÃO ACADÊMICA', heading_style))
content.append(Paragraph("Engenharia de Software – Universidade Cruzeiro do Sul (08/2024 - 12/2026)", normal_style))
content.append(Paragraph("Técnico em Administração – Universidade Eniac (02/2016 - 12/2017)", normal_style))
content.append(Paragraph("Técnico em Logística – Universidade Eniac (12/2017 - 12/2018)", normal_style))
content.append(Paragraph("CAI em Eletricista de Manutenção Eletroeletrônica – Senai (02/2023 - 12/2024)", normal_style))
content.append(Spacer(1, 12))

# Adicionando Experiência Profissional
content.append(Paragraph('EXPERIÊNCIA PROFISSIONAL', heading_style))
content.append(Paragraph("Phibro Animal Health – Aprendiz de Eletricista de Manutenção Eletroeletrônica (02/2023 – 12/2024)", normal_style))
content.append(Paragraph("- Organização e controle de documentação técnica, ordens de serviço e laudos elétricos.", normal_style))
content.append(Paragraph("- Suporte no planejamento e execução de manutenções preventivas e corretivas.", normal_style))
content.append(Paragraph("- Monitoramento de cronogramas e indicadores de desempenho.", normal_style))
content.append(Paragraph("- Gestão de compras e controle de materiais elétricos.", normal_style))
content.append(Paragraph("- Suporte técnico e atendimento ao cliente interno.", normal_style))
content.append(Spacer(1, 12))

# Habilidades e Competências
content.append(Paragraph('HABILIDADES E COMPETÊNCIAS', heading_style))
content.append(Paragraph("Linguagens de Programação: Python, C#, Java, HTML, CSS, JavaScript", normal_style))
content.append(Paragraph("Desenvolvimento e Gestão: Controle de Documentação, Planejamento Estratégico, Gestão de Processos", normal_style))
content.append(Paragraph("Ferramentas: Jira, Excel Avançado, Power BI, AutoCAD", normal_style))
content.append(Paragraph("Infraestrutura e Redes: Redes e Protocolos de Comunicação (Básico)", normal_style))
content.append(Spacer(1, 12))

# Certificações
content.append(Paragraph('CERTIFICAÇÕES', heading_style))
content.append(Paragraph("Desenvolvimento Web Completo – Udemy", normal_style))
content.append(Paragraph("Python Básico ao Avançado – Udemy", normal_style))
content.append(Paragraph("Python Completo – Danki Code", normal_style))
content.append(Paragraph("Lógica de Programação – Senai", normal_style))
content.append(Paragraph("Excel Avançado – Fundação Bradesco", normal_style))
content.append(Paragraph("Desenho Técnico e Sistemas Eletrônicos Digitais – AutoDesk", normal_style))
content.append(Paragraph("Adobe Photoshop, Illustrator e Dreamweaver – Colégio Serrano Guardia", normal_style))
content.append(Spacer(1, 12))

# Idiomas
content.append(Paragraph('IDIOMAS', heading_style))
content.append(Paragraph("Inglês: Intermediário (Leitura e escrita intermediária, conversação básica)", normal_style))
content.append(Spacer(1, 12))

# Informações Adicionais
content.append(Paragraph('INFORMAÇÕES ADICIONAIS', heading_style))
content.append(Paragraph("Interesse e aprendizado contínuo em TI, programação e desenvolvimento de sistemas.", normal_style))

# Adicionando o conteúdo no PDF
doc.build(content)

print("Curriculo Enuk PDF gerado com sucesso!")
