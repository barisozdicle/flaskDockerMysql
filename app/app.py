from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    articles = [{"id": 1, "name": "baris"}, {"id": 2, "name": "gizem"}]

    return jsonify(articles)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
