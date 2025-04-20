from typing import Dict
from src.errors.types.http_bad_request import HttpBadRequest
from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unauthorized import HttpUnauthorized


def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpBadRequest, HttpNotFound, HttpUnauthorized)):
        return {
            "status_code": error.status_code,
            "body": {"errors": [{"title": error.name, "detail": error.message}]},
        }

    return {
        "status_code": 500,
        "body": {"errors": [{"title": "InternalServerError", "detail": str(error)}]},
    }
