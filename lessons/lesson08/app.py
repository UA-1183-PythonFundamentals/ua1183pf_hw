# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!!!!!"

@app.route("/<name>")
def hello2(name):
    return f"Hello, World!!!!!!{name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")