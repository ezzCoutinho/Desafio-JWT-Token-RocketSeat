from abc import ABC, abstractmethod
from typing import Dict


class OrderHistoryControllerInterface(ABC):
    @abstractmethod
    def add_order_to_user(self, user_id: str, order: str) -> Dict:
        pass
