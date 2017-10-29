from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import jsonify
import urllib3
import json
from GetRating import GetSentiment 
from GetKeyWords import GetKeyWords

app = Flask(__name__)
api = Api(app)

class question1(Resource):
    def post(self):
        body = json.loads(request.data)
        return GetSentiment(body["text"])

class question2(Resource):
    def post(self):
        body = json.loads(request.data)
        return GetSentiment(body["text"])

class question3(Resource):
    def post(self):
        body = json.loads(request.data)
        return GetKeyWords(body["text"])


api.add_resource(question1, '/question1') # Route_1
api.add_resource(question2, '/question2') # Route_2
api.add_resource(question3, '/question3') # Route_3

if __name__ == '__main__':
     #app.run(port='5000')
     app.run(host='0.0.0.0', port='5000')