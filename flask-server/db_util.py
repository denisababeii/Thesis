import mysql.connector
import pandas as pd

class DatabaseUtils:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="elective_recommender")
    
    def get_connection(self):
        return self.conn

    def do_login(self, username, password):
        record = (username, password)
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT id FROM `users` WHERE username=%s AND password=%s
            ''', record
        )
        cursor.fetchall()
        if cursor.rowcount != 0:
            cursor.close()
            return "OK"
        else:
            cursor.close()
            return "FAIL"

    def do_signup(self, username, password):
        record = (username, password)
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT id FROM `users` WHERE username=%s
            ''', (username,)
        )
        cursor.fetchall()
        if cursor.rowcount != 0:
            cursor.close()
            return "FAIL"
        else:
            cursor.execute(
            '''
            INSERT INTO `users`(`username`, `password`) VALUES (%s,%s)
            ''', record
            )
            self.conn.commit()
            cursor.close()
            return "OK"

        
    def save_grades(self, username, grades):
        grades = ",".join(str(item) for item in grades)
        record = (grades, username)
        cursor = self.conn.cursor()
        cursor.execute(
        '''
        UPDATE `users` SET grades=%s WHERE username=%s
        ''', record
        )
        self.conn.commit()
        cursor.close()
        return "OK"

    def save_preference(self, username, preference):
        preference = ",".join(str(item) for item in preference)
        record = (preference, username)
        cursor = self.conn.cursor()
        cursor.execute(
        '''
        UPDATE `users` SET preference=%s WHERE username=%s
        ''', record
        )
        self.conn.commit()
        cursor.close()
        return "OK"
    
    def save_result(self, username, result):
        result = ";".join(str(item) for item in result)
        record = (result, username)
        cursor = self.conn.cursor()
        cursor.execute(
        '''
        UPDATE `users` SET result=%s WHERE username=%s
        ''', record
        )
        self.conn.commit()
        cursor.close()
        return "OK"

    def get_grades(self, username):
        grades = []
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT grades FROM `users` WHERE username=%s
            ''', (username,)
        )
        grades_string = cursor.fetchone()
        grades = [int(x) for x in grades_string[0].decode().split(",")]
        cursor.close()
        return grades

    def get_preference(self, username):
        preference = []
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT preference FROM `users` WHERE username=%s
            ''', (username,)
        )
        preference_string = cursor.fetchone()
        preference = preference_string[0].decode().split(",")
        cursor.close()
        return preference

    def get_result(self, username):
        result = []
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT result FROM `users` WHERE username=%s
            ''', (username,)
        )
        result_string = cursor.fetchone()
        if cursor.rowcount == 0:
            cursor.close()
            return result
        result = result_string[0].decode().split(";")
        cursor.close()
        return result

    def get_courses(self):
        query = '''SELECT * FROM `courses`'''
        df = pd.read_sql(query, self.conn)
        return df

    def get_generated_grades(self):
        query = '''SELECT * FROM `grades`'''
        df = pd.read_sql(query, self.conn)
        return df