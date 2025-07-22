import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados salvos pelo scraping
df = pd.read_csv("vagas_fake.csv")

print("✅ Dataset carregado com sucesso!")
print(df.head())

# ==========================
# 📍 Análise 1: Vagas por localidade
# ==========================
vagas_por_local = df["local"].value_counts().head(10)
print("\n🌍 Top 10 localidades com mais vagas:")
print(vagas_por_local)

# Gráfico
plt.figure(figsize=(10, 6))
sns.barplot(x=vagas_por_local.values, y=vagas_por_local.index, palette="viridis")
plt.title("Top 10 Localidades com Mais Vagas")
plt.xlabel("Número de Vagas")
plt.ylabel("Local")
plt.tight_layout()
plt.savefig("grafico_vagas_por_local.png")
plt.show()

# ==========================
# 📍 Análise 2: Empresas que mais aparecem
# ==========================
vagas_por_empresa = df["empresa"].value_counts().head(10)
print("\n🏢 Top 10 empresas com mais vagas:")
print(vagas_por_empresa)

# Gráfico
plt.figure(figsize=(10, 6))
sns.barplot(x=vagas_por_empresa.values, y=vagas_por_empresa.index, palette="magma")
plt.title("Top 10 Empresas com Mais Vagas")
plt.xlabel("Número de Vagas")
plt.ylabel("Empresa")
plt.tight_layout()
plt.savefig("grafico_vagas_por_empresa.png")
plt.show()

# ==========================
# (Extra) Palavras mais comuns nos títulos
# ==========================
from collections import Counter

all_words = " ".join(df["titulo"].tolist()).lower().split()
common_words = Counter(all_words)
mais_comuns = common_words.most_common(10)

print("\n📝 Palavras mais comuns nos títulos de vaga:")
for palavra, qtd in mais_comuns:
    print(f"{palavra}: {qtd}")
