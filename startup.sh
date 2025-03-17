#!/bin/bash
source venv/bin/activate
gunicorn --bind=0.0.0.0:5000 backend.routes:app &
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0