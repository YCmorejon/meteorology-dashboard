import streamlit as st

# Configuración básica
st.set_page_config(page_title="Aplicación Meteorológica", page_icon="⛅",layout="wide")

# Define las páginas
dashboard_page = st.Page("dashboard.py", title="Dashboard", icon="📊")
informe_page = st.Page("informe.py", title="Generar Informe", icon="📝")

# Set up navigation
nav = st.navigation([dashboard_page, informe_page])

# Run the selected page
nav.run()