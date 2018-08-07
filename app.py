from resource.confirm_token import Amil
from flask import Flask
from flask_restful import Api

app = Flask(__name__)

api = Api(app)

api.add_resource(Amil, '/amil')

if __name__ == '__main__':
    app.run(debug=True)
