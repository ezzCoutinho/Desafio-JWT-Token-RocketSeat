import json
from sqlite3 import Connection
from typing import Optional, Tuple

from src.errors.types.http_bad_request import HttpBadRequest
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
            SELECT order_history
            FROM users
            WHERE id = ?
            """,
            (user_id,),
        )

        current_order_history = cursor.fetchone()[0]
        try:
            order_history_list = json.loads(current_order_history)
        except:
            order_history_list = []
        try:
            new_order = json.loads(order)
        except:
            new_order = order

        order_history_list.append(new_order)

        updated_order_history = json.dumps(order_history_list)

        cursor.execute(
            """
            UPDATE users
            SET order_history = ?
            WHERE id = ?
            """,
            (updated_order_history, user_id),
        )
        self.__connection.commit()

    def get_user_by_username_or_id(
        self, username: Optional[str] = None, user_id: Optional[str] = None
    ) -> Tuple[int, str, str, str]:
        cursor = self.__connection.cursor()

        if username:
            cursor.execute(
                """
                SELECT id, username, password, order_history
                FROM users
                WHERE username = ?
                """,
                (username,),
            )
        elif user_id:
            cursor.execute(
                """
                SELECT id, username, password, order_history
                FROM users
                WHERE id = ?
                """,
                (user_id,),
            )
        else:
            raise HttpBadRequest("username or user_id must be provided")

        return cursor.fetchone()
