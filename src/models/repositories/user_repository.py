from sqlite3 import Connection
from typing import Tuple

from src.models.interfaces.user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, connection: Connection) -> None:
        self.__connection = connection

    def registry_user(self, username: str, password: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
            INSERT INTO users
            (username, password, order_history)
            VALUES (?, ?, ?)
            """,
            (username, password, "[]"),
        )
        self.__connection.commit()

    def add_order_to_user(self, user_id: str, order: str) -> None:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
            UPDATE users
            SET order_history = ?
            WHERE id = ?
            """,
            (order, user_id),
        )
        self.__connection.commit()

    def get_user_by_username(self, username: str) -> Tuple[int, str, str, str]:
        cursor = self.__connection.cursor()
        cursor.execute(
            """
            SELECT id, username, password, order_history
            FROM users
            WHERE username = ?
            """,
            (username,),
        )
        return cursor.fetchone()
