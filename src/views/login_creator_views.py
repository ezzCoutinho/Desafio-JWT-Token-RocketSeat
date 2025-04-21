from src.controllers.interfaces.login_creator_controller_interface import (
    LoginCreatorControllerInterface,
)
from src.errors.types.http_bad_request import HttpBadRequest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")  # type: ignore
        password = http_request.body.get("password")  # type: ignore

        self.__validate_inputs(username, password)  # type: ignore

        response = self.__controller.create(username, password)  # type: ignore

        return HttpResponse(status_code=200, body=response)

    def __validate_inputs(self, username: str, password: str) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise HttpBadRequest("Invalid Input")
