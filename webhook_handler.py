from flask import Flask, request, jsonify
import subprocess
import threading
import os

app = Flask(__name__)
REPO_PATH = "/home/admin/catty-reminders-app"  # <-- замените admin на вашего пользователя
VENV_PIP = f"{REPO_PATH}/venv/bin/pip"

def deploy():
    try:
        subprocess.run(["git", "pull"], cwd=REPO_PATH, check=True)
        subprocess.run([VENV_PIP, "install", "-r", "requirements.txt"], cwd=REPO_PATH, check=True)
        subprocess.run(["sudo", "systemctl", "restart", "catty-reminders"], check=True)
        print("✅ Успешный деплой")
    except Exception as e:
        print(f"❌ Ошибка деплоя: {e}")

@app.route("/", methods=["POST"])
def webhook():
    payload = request.get_json()
    if payload and payload.get("ref"):
        threading.Thread(target=deploy).start()
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
