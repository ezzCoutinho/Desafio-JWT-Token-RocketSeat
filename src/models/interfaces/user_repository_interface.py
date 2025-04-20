from abc import ABC, abstractmethod
from typing import Optional, Tuple


class UserRepositoryInterface(ABC):
    @abstractmethod
    def registry_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> Tuple[int, str, str, str]:
        pass

    @abstractmethod
    def add_order_to_user(self, user_id: str, order: str) -> None:
        pass
