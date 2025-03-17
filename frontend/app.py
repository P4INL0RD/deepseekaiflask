import streamlit as st
import requests

# 🔹 Usa la URL de tu backend en Azure (cambia esto con la URL real)
BACKEND_URL = "https://deepseekbot-a5gbcjg7aee2g8c8.canadacentral-01.azurewebsites.net/"

st.set_page_config(page_title="ChatBot DeepSeek R-1", layout="wide")
st.title("🤖 ChatBot DeepSeek R-1")

# Interfaz de chat
st.subheader("Chat con IA")
user_input = st.text_input("Escribe tu mensaje:")

if st.button("Enviar"):
    if user_input:
        with st.spinner("Procesando..."):
            try:
                response = requests.post(f"{BACKEND_URL}/chat", json={"message": user_input}, timeout=10)
                if response.status_code == 200:
                    st.text_area("Respuesta:", response.json().get("response", "No se recibió respuesta"), height=200)
                else:
                    st.text_area("Respuesta:", f"Error {response.status_code}: {response.text}", height=200)
            except requests.exceptions.RequestException as e:
                st.text_area("Respuesta:", f"Error de conexión: {str(e)}", height=200)

# Subir archivos para resumen
st.subheader("📂 Subir archivo para resumir")
uploaded_file = st.file_uploader("Elige un archivo", type=["pdf", "docx", "txt", "csv"])

if uploaded_file:
    with st.spinner("Procesando el resumen..."):
        try:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            response = requests.post(f"{BACKEND_URL}/summarize", files=files, timeout=30)
            if response.status_code == 200:
                summary = response.json().get("summary", "No se pudo generar el resumen")
                st.text_area("Resumen generado:", summary, height=200)
                
                # Botón para descargar el resumen
                st.download_button(
                    label="Descargar Resumen",
                    data=summary,
                    file_name="resumen.txt",
                    mime="text/plain"
                )
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error de conexión: {str(e)}")
