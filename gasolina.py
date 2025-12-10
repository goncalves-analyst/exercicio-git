import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler os dados
data = pd.read_csv('gasolina.csv')

# Criar o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='dia', y='venda')
plt.title('Preço da Gasolina em SP (Julho 2021)')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')

# Salvar a imagem
plt.savefig('gasolina.png')
print("Gráfico salvo com sucesso!")
