
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square')
def square():
    try:
        x = float(request.args.get("x", 0))
        return jsonify({"x": x, "square": x ** 2})
    except ValueError:
        return jsonify({"error": "Niepoprawna wartość x"}), 400

if __name__ == '__main__':
    app.run(port=5002)
