import streamlit as st
import requests


API_URL = "http://localhost:5000/chat"  # Cambia a la URL de tu backend en Azure

st.title("ChatBot DeepSeek R-1")

# Input de texto para consultas de chat
user_input = st.text_input("Escribe tu consulta:")

if user_input:
    response = requests.post(f"{API_URL}/chat", json={"input": user_input})
    st.write(response.json().get('response'))

# Subida de archivos
file = st.file_uploader("Sube tu archivo", type=["pdf", "docx", "txt", "csv"])

if file:
    response = requests.post(f"{API_URL}/upload", files={"file": file})
    st.write(response.json().get('summary'))

