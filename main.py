from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
dados = [{'nome':'filipe'},{'idade':18}]
class HelloWord(Resource):
    def get(self):
        return {'Hello':'world'}


class Dados(Resource):
    def get(self):
        return dados[0]
#api.add_resource(HelloWord,'/')

api.add_resource(Dados,'/')

app.run(host='0.0.0.0', port=81)
