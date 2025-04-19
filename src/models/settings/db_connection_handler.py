import sqlite3
from sqlite3 import Connection
from typing import Optional


class __DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__connection = None

    def connect(self) -> None:
        self.__connection = sqlite3.connect(
            self.__connection_string, check_same_thread=False
        )

    def get_connection(self) -> Optional[Connection]:
        return self.__connection


db_connection_handler = __DbConnectionHandler()
