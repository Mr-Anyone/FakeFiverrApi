from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name): # Being able to access a name variable that is defined
        return {"data" : name, "Page": "1"}

api.add_resource(HelloWorld, "/helloworld/<string:name>") # using hellowrold but a string parm is added

if __name__ == "__main__" :
    app.run(debug=True)