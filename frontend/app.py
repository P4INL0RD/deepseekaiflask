import streamlit as st
import requests

# Configurar la URL del backend Flask
BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="ChatBot DeepSeek R-1", layout="wide")

# Forzar Streamlit a ignorar preloads de fuentes personalizadas
st.markdown(
    """
    <style>
        * {
            font-family: sans-serif !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 ChatBot DeepSeek R-1")

# Interfaz de chat
st.subheader("Chat con IA")
user_input = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    if user_input:
        response = requests.post(f"{BACKEND_URL}/chat", json={"message": user_input})
        st.text_area("Respuesta:", response.json().get("response", "Error en la respuesta"), height=200)

# Subir archivos para resumen
st.subheader("📂 Subir archivo para resumir")
uploaded_file = st.file_uploader("Elige un archivo", type=["pdf", "docx", "txt", "csv"])
if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    response = requests.post(f"{BACKEND_URL}/summarize", files=files)
    summary = response.json().get("summary", "No se pudo generar el resumen")
    st.text_area("Resumen generado:", summary, height=200)
    
    # Botón para descargar el resumen
    st.download_button(
        label="Descargar Resumen",
        data=summary,
        file_name="resumen.txt",
        mime="text/plain"
    )
