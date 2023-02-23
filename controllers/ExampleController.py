
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/getexample', methods=['GET'])
def get_all_examples():
    return jsonify(exampleService.getAllExamples())

@app.route('/postexample', methods=['POST'])
def save_example():
    example = request.get_json()
    return jsonify(exampleService.saveExample(example))