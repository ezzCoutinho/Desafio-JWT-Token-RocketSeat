from src.controllers.interfaces.order_history_controller_interface import (
    OrderHistoryControllerInterface,
)
from src.errors.types.http_bad_request import HttpBadRequest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class OrderHistoryView(ViewInterface):
    def __init__(self, controller: OrderHistoryControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        order_history = http_request.body.get("order_history")  # type: ignore
        user_id = http_request.params.get("user_id")  # type: ignore
        headers_user_id = http_request.token_info.get("user_id")  # type: ignore

        self.__validate_inputs(user_id, order_history, headers_user_id)  # type: ignore
        response = self.__controller.add_order_to_user(user_id, order_history)  # type: ignore
        return HttpResponse(status_code=200, body=response)

    def __validate_inputs(
        self, user_id: str, order_history: str, headers_user_id: str
    ) -> None:
        if (
            not user_id
            or not order_history
            or not isinstance(order_history, str)
            or int(headers_user_id) != int(user_id)
        ):
            raise HttpBadRequest("Invalid Input")
