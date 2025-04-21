from flask import request

from src.drivers.jwt_handler import JwtHandler
from src.errors.types.http_unauthorized import HttpUnauthorized


def auth_jwt_verify():
    jwt_handler = JwtHandler()
    raw_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    if not raw_token or not user_id:
        raise HttpUnauthorized("Invalid Auth Informations")

    token = raw_token.split()[1]
    token_information = jwt_handler.decode_jwt_token(token)
    token_uid = token_information.get("user_id")

    if user_id and token_uid and (int(token_uid) == int(user_id)):
        return token_information

    raise HttpUnauthorized("User not authorized")
