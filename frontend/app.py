import streamlit as st
import requests

# URL del backend en Azure
BACKEND_URL = "https://deepseekbot-a5gbcjg7aee2g8c8.canadacentral-01.azurewebsites.net/"  # Reemplaza con la URL real
API_KEY = "2Ss0sjP9U6f0ronN6JAlZ4bnEOcAE6njPMZFPqOSUec1reyILr5CJQQJ99BCACYeBjFXJ3w3AAAAACOGOFRS"  # Reemplaza con tu clave de API

st.set_page_config(page_title="ChatBot DeepSeek R-1", layout="wide")
st.title("🤖 ChatBot DeepSeek R-1")

# Interfaz de chat
st.subheader("Chat con IA")
user_input = st.text_input("Escribe tu mensaje:")

if st.button("Enviar"):
    if user_input:
        headers = {"Authorization": f"Bearer {API_KEY}"}  # Agrega la API Key en los headers
        response = requests.post(f"{BACKEND_URL}/chat", json={"message": user_input}, headers=headers)

        if response.status_code == 200:
            try:
                response_data = response.json()
                st.text_area("Respuesta:", response_data.get("response", "Error en la respuesta"), height=200)
            except requests.exceptions.JSONDecodeError:
                st.error("Error: La respuesta del servidor no es un JSON válido.")
        else:
            st.error(f"Error {response.status_code}: {response.text}")  # Muestra el error detallado
