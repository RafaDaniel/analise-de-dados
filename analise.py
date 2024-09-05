import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("fatura.csv")
dados.head()

valor_total_cartao = dados["ValorCompra"].sum()
print(valor_total_cartao)

valor_gasto_por_titular = dados.groupby("Nome")["ValorCompra"].sum().reset_index().sort_values(by="ValorCompra", ascending=True)
valor_gasto_por_titular

valor_gasto_por_categoria = dados.groupby("categoria")["ValorCompra"].sum().reset_index().sort_values(by="ValorCompra", ascending=False)
valor_gasto_por_categoria 

gastos_por_dia = dados.groupby("data_compra")["ValorCompra"].sum().reset_index().sort_values(by="data_compra", ascending=True)
gastos_por_dia

plt.figure(figsize=(10, 6))
plt.bar(valor_gasto_por_titular["Nome"], valor_gasto_por_titular["ValorCompra"], color="red")
plt.title("Valor gasto por titular")
plt.xlabel("Nome")
plt.ylabel("Valor")
plt.show()

plt.figure(figsize=(10, 6))
plt.barh(valor_gasto_por_categoria["categoria"], valor_gasto_por_categoria["ValorCompra"])
plt.xlabel("Valor da Compra")
plt.ylabel("Categoria")
plt.gca().invert_yaxis()
plt.show()

plt.figure(figsize=(5, 5))
plt.pie(valor_gasto_por_titular["ValorCompra"], labels= valor_gasto_por_titular["Nome"], autopct="%1.2f%%")
plt.title("Distribuição de gastos por titular")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(gastos_por_dia["data_compra"], gastos_por_dia["ValorCompra"], marker="o", linestyle="-", color="b")
plt.title("Gastos ao longo do tempo")
plt.xlabel("Data")
plt.ylabel("Valor")
plt.xticks(rotation=45)
plt.show()
