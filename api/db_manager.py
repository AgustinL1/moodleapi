# Module Imports
import sys
import mariadb

class DBManager:

    _conn = None
    _cur = None
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = DBManager()
        return cls._instance


    def __init__(self):
        try:
            self._conn = mariadb.connect(
                user="bn_moodle",
                password="",
                host="mariadb",
                port=3306,
                database="bitnami_moodle"
            )
            print("Connected to DB")

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        self._cur = self._conn.cursor() 

    def get_cur(self):
        return self._cur

    def commit(self):
        self._conn.commit()

    def hola(self):
        print("Hola")