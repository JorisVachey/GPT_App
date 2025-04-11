import subprocess
import webbrowser
import time
import os
import sys

def get_app_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
        return os.path.join(base_path, "GPT.py")
    else:
        return os.path.abspath("GPT.py")

app_path = get_app_path()

# Utilise sys.executable pour la compatibilité Windows / macOS
process = subprocess.Popen([sys.executable, "-m", "streamlit", "run", app_path])

time.sleep(5)
webbrowser.open("http://localhost:8501")

print("✅ App en cours... Appuie sur Ctrl+C pour quitter.")
process.wait()
