import streamlit as st

st.markdown(
    """
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <div style="display:flex;align-items:center;gap:10px;
                background:#f8f9fa;padding:15px;border-radius:12px;
                box-shadow:0 2px 6px rgba(0,0,0,0.1);">
        <i class="material-icons" style="font-size:36px;color:#f39c12;">thermostat</i>
        <div>
            <div style="font-size:14px;color:#555;">Temperatura</div>
            <div style="font-size:22px;font-weight:bold;">25°C</div>
            <div style="font-size:12px;color:green;">+2°C</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
