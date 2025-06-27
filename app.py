
import streamlit as st
from database import criar_tabela, inserir_produto, listar_produtos
from validade import produtos_vencidos, produtos_a_vencer
from datetime import datetime

criar_tabela()

st.title("🧊 Controle de Validade - Hipermercado")

menu = st.sidebar.selectbox("Menu", ["Cadastrar Produto", "Visualizar Produtos", "Alertas de Validade"])

if menu == "Cadastrar Produto":
    st.subheader("📦 Cadastro de Produto")
    nome = st.text_input("Nome do produto")
    codigo_barras = st.text_input("Código de barras")
    data_validade = st.date_input("Data de validade")
    categoria = st.text_input("Categoria")
    localizacao = st.text_input("Localização (ex: Gôndola 4)")

    if st.button("Salvar"):
        inserir_produto(nome, codigo_barras, data_validade, categoria, localizacao)
        st.success("✅ Produto cadastrado com sucesso!")

elif menu == "Visualizar Produtos":
    st.subheader("📋 Lista de Produtos")
    produtos = listar_produtos()
    st.dataframe(produtos)

elif menu == "Alertas de Validade":
    st.subheader("🚨 Produtos Vencidos / Quase Vencendo")
    dias_alerta = st.slider("Dias para alerta de vencimento", 1, 90, 30)
    produtos = listar_produtos()
    vencidos = produtos_vencidos(produtos)
    a_vencer = produtos_a_vencer(produtos, dias_alerta)

    st.write(f"🔴 Produtos Vencidos ({len(vencidos)}):")
    st.dataframe(vencidos)

    st.write(f"🟠 Produtos a vencer em até {dias_alerta} dias ({len(a_vencer)}):")
    st.dataframe(a_vencer)
