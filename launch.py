import subprocess
import webbrowser
import time
import os
import sys

def get_app_path():
    if getattr(sys, 'frozen', False):
        # Si compilé avec PyInstaller
        base_path = sys._MEIPASS
        return os.path.join(base_path, "GPT.py")
    else:
        # Si lancé en mode normal
        return os.path.abspath("GPT.py")

app_path = get_app_path()

# Lancer Streamlit
process = subprocess.Popen(["python", "-m", "streamlit", "run", app_path])

# Attendre un peu que le serveur démarre
time.sleep(5)

# Ouvrir le navigateur
webbrowser.open("http://localhost:8501")

# Garder le terminal ouvert
print("App en cours... Appuie sur ctrl+c pour quitter.")
process.wait()
