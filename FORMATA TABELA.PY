import streamlit as st
import pandas as pd

st.set_page_config(page_title="Formatador de Tabela", layout="centered")

st.title("?? Formatador de Tabela com Prefixo e Sufixo")

prefixo = st.text_input("?? Prefixo", value="PROV REF")
sufixo = st.text_input("?? Sufixo", value="FOPAG BHZ ADM 08/25")
textos = st.text_area("?? Cole os textos aqui (um por linha)", height=300)

if st.button("?? Gerar Tabela"):
    if not textos.strip():
        st.warning("Por favor, cole os textos no campo acima.")
    else:
        linhas = [linha.strip() for linha in textos.strip().split('\n') if linha.strip()]
        dados = []
        for linha in linhas:
            descricao = f"{prefixo} {linha} {sufixo}"
            dados.append([descricao, ""])
        
        df = pd.DataFrame(dados, columns=["Descrição", "Valor"])
        st.success("? Tabela gerada com sucesso!")
        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("?? Baixar como CSV", data=csv, file_name="tabela_formatada.csv", mime="text/csv")