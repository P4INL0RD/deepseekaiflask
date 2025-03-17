from app import create_app
import subprocess

app = create_app()

if __name__ == '__main__':
    subprocess.Popen(['streamlit', 'run', 'frontend/app.py'])
    app.run(debug=True, use_reloader=False)