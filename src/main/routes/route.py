from flask import Blueprint, jsonify, request

from src.composer.login_creator_composer import login_creator_composer
from src.composer.order_history_composer import order_history_composer
from src.composer.user_register_composer import user_register_composer
from src.errors.error_controller import handle_errors
from src.main.middlewares.auth_jwt import auth_jwt_verify
from src.views.http_types.http_request import HttpRequest

ifood_fake = Blueprint("ifood_fake", __name__)


@ifood_fake.route("/ifood/registry", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        response = handle_errors(error)
        return jsonify(response["body"]), response["status_code"]


@ifood_fake.route("/ifood/login", methods=["POST"])
def login():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        response = handle_errors(error)
        return jsonify(response["body"]), response["status_code"]


@ifood_fake.route("/ifood/order/<user_id>", methods=["POST"])
def order(user_id: str):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(
            body=request.json,
            params={"user_id": user_id},
            token_info=token_information,
            headers=request.headers,
        )
        http_response = order_history_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        response = handle_errors(error)
        return jsonify(response["body"]), response["status_code"]
