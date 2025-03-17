import subprocess
import threading

def run_flask():
    subprocess.run(["python", "app/routes.py"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "frontend/app.py"])

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    threading.Thread(target=run_streamlit).start()
