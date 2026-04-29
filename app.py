import streamlit as st
import pandas as pd
import random

# Configuração inicial da página
st.set_page_config(page_title="Dashboard Maker", page_icon="🤖", layout="wide")

st.title("📡 Dashboard Maker: Monitor de Sensores")
st.write("Visualize os dados do seu ambiente como um verdadeiro cientista de dados!")

# MEMÓRIA (Variáveis de Estado) - Onde guardamos os dados (como as variáveis globais do Arduino!)
if 'dados_sensores' not in st.session_state:
    st.session_state.dados_sensores = pd.DataFrame(columns=["Temperatura", "Umidade", "Luminosidade"])

# Botão para simular a leitura (como um digitalRead ou analogRead)
if st.button("🔄 Ler Sensores Agora"):
    nova_leitura = {
        "Temperatura": random.uniform(20.0, 35.0),
        "Umidade": random.uniform(40.0, 80.0),
        "Luminosidade": random.randint(100, 1000)
    }
    
    nova_linha = pd.DataFrame([nova_leitura])
    st.session_state.dados_sensores = pd.concat([st.session_state.dados_sensores, nova_linha], ignore_index=True)

# Só mostra os gráficos se tivermos dados gravados
if not st.session_state.dados_sensores.empty:
    
    ultima_temp = st.session_state.dados_sensores["Temperatura"].iloc[-1]
    ultima_umid = st.session_state.dados_sensores["Umidade"].iloc[-1]
    ultima_luz = st.session_state.dados_sensores["Luminosidade"].iloc[-1]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="🌡️ Temperatura", value=f"{ultima_temp:.1f} °C")
    with col2:
        st.metric(label="💧 Umidade", value=f"{ultima_umid:.1f} %")
    with col3:
        st.metric(label="☀️ Luminosidade", value=f"{ultima_luz} lux")
        
    st.divider() 
    
    st.subheader("📈 Histórico de Leituras")
    st.line_chart(st.session_state.dados_sensores)
    
else:
    st.info("👆 Clique no botão acima para iniciar a leitura dos sensores!")

