from abc import ABC, abstractmethod
from typing import Dict


class UserRegisterControllerInterface(ABC):
    @abstractmethod
    def registry_user(self, username: str, password: str) -> Dict:
        pass
