from flask import Flask

from src.main.routes.route import ifood_fake
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()


app = Flask(__name__)

app.register_blueprint(ifood_fake)
