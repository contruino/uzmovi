from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)
class Home(Resource):
    def get(self, name):
        return {'ism':name}

api.add_resource(Home, "/<string:name>")

app.run(debug=True)