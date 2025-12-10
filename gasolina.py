import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
grafico = sns.lineplot(data=df, x='dia', y='venda', marker='o')
grafico.set_title('Preço Médio da Gasolina em SP (Julho 2021)', fontsize=16)
grafico.set_xlabel('Dia', fontsize=12)
grafico.set_ylabel('Preço (R$)', fontsize=12)

plt.savefig('gasolina.png')
