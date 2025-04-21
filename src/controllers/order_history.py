import json
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
        user = self.__user_repository.get_user_by_username_or_id(user_id=user_id)
        order_history = user[3]

        try:
            order_history_list = json.loads(order_history)
        except:
            order_history_list = []

        return {
            "type": "User",
            "count": len(order_history_list),
            "order_history": order_history_list,
        }
