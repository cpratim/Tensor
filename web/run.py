from flask import Flask, jsonify, request, render_template, send_file
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

@api.route('/api/contribute', methods=['POST'])
def contribute():
    json = request.get_json()
    return

@api.route('/query', methods=['GET'])
def query():
    return render_template('query.html')

@api.route('/')
def login():
    return render_template('login.html')


@api.route('/upload')
def upload():
    return render_template('upload.html')

@api.route('/thank_you', methods=['GET'])
def thank_you():
    return render_template('thank_you.html')

@api.route('/sample_query.json', methods=['GET'])
def sample_query():
    return send_file('sample_query.json')


if __name__ == '__main__':
    api.run(debug=True)