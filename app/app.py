from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", temp=42)


@app.route("/api/<location>")
def api(location):
    return jsonify(f"Hello, {location}")
