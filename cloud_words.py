import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Frases hipotéticas de avaliações de clientes:
frases = ('Eu simplesmente adorei o serviço prestado! A equipe foi extremamente profissional, atenciosa e eficiente. Recomendo a todos', 'Fiquei impressionado com a qualidade do produto que recebi. Além de ser exatamente o que eu estava procurando, a entrega foi super rápida. Estou muito satisfeito!', 'Excelente experiência! O atendimento ao cliente foi impecável, o ambiente era acolhedor e o produto final superou todas as minhas expectativas. Certamente voltarei!', 'Infelizmente, tive uma experiência decepcionante com essa empresa. O produto que recebi estava danificado e o suporte ao cliente foi extremamente lento para resolver o problema. Não recomendaria.')

# Juntando as frases em uma única string
frases_str = ' '.join(frases)

# Gerando nuvem de palavras:
nuvem = WordCloud(
    background_color='black',
    width=1600,
    height=600
).generate(frases_str)

# Criando um gráfico para mostrar a nuvem
fig, ax = plt.subplots(figsize=(10, 7))
ax.imshow(nuvem, interpolation='bilinear')
ax.set_axis_off()  # para não aparecer as linhas do gráfico
plt.show()