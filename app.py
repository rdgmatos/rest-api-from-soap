from datetime import datetime
from utils.logger import logger
from resource.token import Amil
from flask import Flask
from utils.cache import cache
from flask_restful import Api

app = Flask(__name__)

api = Api(app)

api.add_resource(Amil, '/amil')

if __name__ == '__main__':
    logger.info("Starting app %s", datetime.now())
    cache.init_app(app)
    app.run(debug=True)
