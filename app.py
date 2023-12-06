from flask import Flask, render_template, jsonify
from controllers.controllers import fetch_github_repos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/github/<username>/repos", methods=["GET"])
def get_github_repos(username):
    result = fetch_github_repos(username)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
    