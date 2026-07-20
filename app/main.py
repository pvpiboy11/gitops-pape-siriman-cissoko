from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    version = os.environ.get('APP_VERSION', 'v1')
    return f"""
    <html>
        <head><title>Pape Siriman Cissoko - GitOps Project</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Pape Siriman Cissoko</h1>
            <p>Application deployee via GitOps sur Kubernetes</p>
            <p>Version: {version}</p>
            <p>Pod: {hostname}</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)