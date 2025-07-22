import streamlit as st
import pandas as pd

# Carregar os dados
df = pd.read_csv("vagas_fake.csv")

# Título do app
st.title("📊 Dashboard de Vagas - Fake Jobs")

st.markdown("Exibindo dados extraídos de [realpython.github.io/fake-jobs](https://realpython.github.io/fake-jobs/)")

# Filtro por localização
localidades = df["local"].unique().tolist()
local_selecionado = st.selectbox("Filtrar por localidade:", ["Todos"] + localidades)

# Filtro por empresa
empresas = df["empresa"].unique().tolist()
empresa_selecionada = st.selectbox("Filtrar por empresa:", ["Todas"] + empresas)

# Aplicar filtros
df_filtrado = df.copy()
if local_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["local"] == local_selecionado]

if empresa_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado["empresa"] == empresa_selecionada]

# Exibir número de vagas e dataframe
st.markdown(f"**🔎 Total de vagas encontradas:** {len(df_filtrado)}")
st.dataframe(df_filtrado)

# Download do CSV filtrado
st.download_button(
    label="⬇️ Baixar CSV com os resultados filtrados",
    data=df_filtrado.to_csv(index=False),
    file_name="vagas_filtradas.csv",
    mime="text/csv"
)

# Exibir links clicáveis
st.markdown("---")
st.markdown("### 🔗 Links para aplicar nas vagas:")

for _, row in df_filtrado.iterrows():
    st.markdown(f"- [{row['titulo']} – {row['empresa']}]({row['link']})")
