#импорт модулей
import mysql.connector as connector
import json, datetime, inspect, DataBase

def create_database(connection, name):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE " + name)
        log("Database created successfully")
    except connector.Error as e:
        log(f"Error {e}", "ConnectionError")

#работа с json (параметр в таблице)
def parsefromjson(jsontext : str) -> dict:
    try:
        return json.loads(jsontext)
    except Exception as e:
        log(str(e), e.__class__.__name__)
        return {}

def parsetojson(dictionary : dict) -> str:
    try:
        return json.dumps(dictionary)
    except Exception as e:
        log(str(e), e.__class__.__name__)
        return ""

#вывод сообщений
def log(message : str = "Empty message", messagetype : str = "", additional : str = "") -> None:
    date = f"{datetime.datetime.now():%d.%m.%Y %H:%M:%S.%f}"
    stack = inspect.stack()[1][1] + ": " + inspect.stack()[1][3]
    basicmessage = date + ": " + stack + ": "
    try:
        if (len(messagetype) > 0): messagetype += ": "
        if (len(additional) > 0): additional = f"<{additional}>"
        with open("log.txt", "a") as file:
            file.writelines(f"{basicmessage} {messagetype} {message} {additional}\n")
            file.close()
    except TypeError as e:
        log(str(e) + "; stack is: " + stack, e.__class__.__name__)
        return
    print(f"{basicmessage} {messagetype} {message}")

#функция выполнения main
def main():
    parsefromjson(None)
    DB = DataBase.DBControler()
    DB = None

if __name__ == "__main__": main()