from flask import Flask
from flask_smorest import Api, Blueprint

server = Flask(__name__)


class APIConfing:
    API_TITLE = 'TODO API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.3'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/docs'
    OPENAPI_SWAGGER_UI_URL = 'https://www.npmjs.com/package/swagger-ui-dist'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_REDOC_UI_URL = 'https://www.jsdelivr.com/package/npm/redoc-ld'


server.config.from_object(APIConfing)

api = Api(server)

todo = Blueprint('todo', 'todo', url_prefix='/todo', description='TODO API')


api.register_blueprint(todo)



