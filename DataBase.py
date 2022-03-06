#
from typing import Any
import mysql.connector as connector, main

#
class DB:
    @property 
    def is_dead(self):
        if self.connection is None: return True
        try:
            self.connection.isolation_level
            return False
        except Exception as e:
            return True
    def __init__(self, connection = None) -> None:
        self.connection = connection
    def commit(self) -> None:
        self.connection.commit()
    def create_connection(host_name : str, user_name : str, user_password : str, db_name : str = None) -> Any:
        connection = None
        try:
            connection = connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            ) if db_name == None else connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            main.log("Connection to MySQL DB successful")
        except connector.Error as e:
            main.log(f"Error {e}", "ConnectionError")
        return connection
    def setconnection(self, connection) -> None:
        self.connection = connection
    def __del__(self):
        if not self.connection is None: 
            try: 
                self.connection.close()
            except Exception as e:
                main.log(str(e), e.__class__.__name__)

#
class DBControler(DB):
    def __init__(self, connection = None) -> None:
        super().__init__(connection)
    def rawexec(self, command : str) -> Any:
        if not self.is_dead: return
        try:
            with self.connection.cursor() as cursor: 
                cursor.execute(command)
                self.commit()
                return cursor
        except Exception as e:
            main.log(str(e), e.__class__.__name__, command)
    def rawmanyexec(self, command : str, args : list) -> Any:
        if not self.is_dead: return
        try:
            with self.connection.cursor() as cursor: 
                cursor.executemany(command)
                self.commit()
                return cursor
        except Exception as e:
            main.log(str(e), e.__class__.__name__, f"{command}:{args}")
    def exec(): pass
    def manyexec(): pass
    def scriptexec(self, command : str) -> Any:
        if not self.is_dead: return
        try:
            with self.connection.cursor() as cursor: 
                cursor.executescript(command)
                self.connection.commit()
                return cursor
        except Exception as e:
            main.log(str(e), e.__class__.__name__, command)
    def getcommandline() -> str:
        pass

#
class DBLoader(DB):
    def __init__(self, connection = None) -> None:
        super().__init__(connection)