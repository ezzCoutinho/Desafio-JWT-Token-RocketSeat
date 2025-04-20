from typing import Dict

from src.controllers.interfaces.order_history_controller_interface import (
    OrderHistoryControllerInterface,
)

from src.models.interfaces.user_repository_interface import UserRepositoryInterface


class OrderHistory(OrderHistoryControllerInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository

    def add_order_to_user(self, user_id: str, order: str) -> Dict:
        self.__user_repository.add_order_to_user(user_id, order)

        return {"type": "User", "count": 1, "order_history": order}
