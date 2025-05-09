from abc import ABC, abstractmethod
from typing import Optional, Tuple


class UserRepositoryInterface(ABC):
    @abstractmethod
    def registry_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def add_order_to_user(self, user_id: str, order: str) -> None:
        pass

    @abstractmethod
    def get_user_by_username_or_id(
        self, username: Optional[str] = None, user_id: Optional[str] = None
    ) -> Tuple[int, str, str, str]:
        pass
