from mysql import connector
from mysql.connector import Error, OperationalError

class DatabaseHandler:
    def __init__(self, host, port, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port' : port,
        }

    def _connect(self):
        try:
            return connector.connect(**self.config)
        except OperationalError as e:
            if "timed out" in str(e).lower():
                raise Exception("Connection timeout")
            raise

    def national_code_exists(self, national_code):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = "SELECT 1 FROM teachers WHERE teacher_national_code = %s"
            cursor.execute(query, (national_code,))
            return cursor.fetchone() is not None
        except Error as e:
            if "read timeout" in str(e).lower():
                raise Exception("Executing timeout")
            raise Exception(f"DB ERROR : {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    def add_teacher(self, first_name, last_name, national_code, password, classes, lesson):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = """INSERT INTO teachers 
                       (teacher_name, teacher_family, teacher_national_code, teacher_password, lesson)
                       VALUES (%s, %s, %s, %s, %s)"""
            query2 = """INSERT INTO teacher_class 
                       ()
                       VALUES (%s, %s, %s, %s, %s, %s)"""
            data = (first_name, last_name, national_code, password, lesson)
            print(data)
            x=cursor.execute(query, data)
            print(x)
            conn.commit()
            return cursor.rowcount == 1
        except Error as e:
            conn.rollback()
            raise Exception(f"ERROR WIHLE ADDING DATA : {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    def get_school_id(self, school_code):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = "SELECT id FROM schools WHERE school_code = %s"
            cursor.execute(query, (school_code,))
            x = cursor.fetchall()[0][0]
            print("cursor result is :")
            return x
        except Error as e:
            if "read timeout" in str(e).lower():
                raise Exception("Executing timeout")
            raise Exception(f"DB ERROR : {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    def get_class_id(self, class_name):
        try:
            conn = self._connect()
            cursor = conn.cursor()
            query = "SELECT id FROM classes WHERE class_name = %s"
            cursor.execute(query, (class_name,))
            print(111)
            return cursor.fetchall()[0][0]
        
        except Error as e:
            if "read timeout" in str(e).lower():
                raise Exception("Executing timeout")
            raise Exception(f"DB ERROR : {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    db = DatabaseHandler(
            host='185.4.28.110',
            database='sap',
            user='root',
            password='sapprogram2583',
            port=5000
        )
    (db.get_school_id('123'))