import streamlit as st


# Barra de búsqueda
col1, col2 = st.columns([4,1])  # Una columna más grande para el input
with col1:
    ubicacion = st.text_input("Escribe una ciudad", placeholder="Ej. Madrid, España",label_visibility="collapsed")
with col2:
    st.button("🔍", use_container_width=True)


# Título principal y subtítulo
st.markdown("<h1 style='text-align: left; color: #1E90FF;'>Tiempo</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: #FFA500;'>Habana,Cuba</h3>", unsafe_allow_html=True)




# Datos meteorológicos
col1, col2 = st.columns(2)

with col1:
    st.metric(label="🌡️ Temperatura", value="25°C")
    st.metric(label="🌬️ Viento", value="15 km/h")
    st.metric(label="💧 Humedad", value="40%")

with col2:
    st.metric(label="🤒 Sensación Térmica", value="27°C")
    st.metric(label="💨 Ráfagas de Viento", value="25 km/h")
    st.metric(label="☁️ Nubes", value="60%")
 

# Estilo adicional
st.markdown(
    """
    <style>
        .stMetric {
            text-align: center !important;
            background-color: #F0F8FF;
            padding: 12px;
            border-radius: 12px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

