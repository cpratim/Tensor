from flask import Flask, jsonify, request
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route('/api/query', methods=['GET'])
def query():
    json = request.get_json()

@api.route('/api/contribute', methods=['POST'])
def contribute():
    json = request.get_json()

@api.route('/api/query', methods=['POST'])
def query():
    json = request.get_json()
    


if __name__ == '__main__':
    api.run(debug=True)