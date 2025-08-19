from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "<h1>LiteJob — кабинет</h1><p>Здесь скоро появится вход через HH.</p>"

@app.get("/health")
def health():
    return {"status": "ok"}
