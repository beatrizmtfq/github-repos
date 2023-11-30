from flask import Flask, render_template, jsonify
from controllers.controllers import get_users_route_handler
from models.models import get_users


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/github/<username>/repos", methods=["GET"])
def get_users_route_handler(username):
    result = get_users_route_handler(username)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
