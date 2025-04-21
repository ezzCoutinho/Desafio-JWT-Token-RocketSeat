from src.controllers.interfaces.user_register_controller_interface import (
    UserRegisterControllerInterface,
)
from src.errors.types.http_bad_request import HttpBadRequest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class UserRegisterViews(ViewInterface):
    def __init__(self, controller: UserRegisterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")  # type: ignore
        password = http_request.body.get("password")  # type: ignore

        self.__validate_inputs(username, password)  # type: ignore

        self.__controller.registry_user(username, password)  # type: ignore

        return HttpResponse(201, {"message": "User registered successfully"})

    def __validate_inputs(self, username: str, password: str) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise HttpBadRequest("Invalid Input")
