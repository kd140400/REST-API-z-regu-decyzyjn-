
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')

    if not name:
        return jsonify({'error': 'Brak parametru "name"'}), 400

    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(port=5001)
