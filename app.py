from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Flask server is running 🚀"
    })

@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({
        "you_sent": data
    })

@app.route("/api/sum", methods=["POST"])
def calculate_sum():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({
        "sum": a + b
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)