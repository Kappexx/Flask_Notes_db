import mysql.connector as myconnect

class Person:
    def __init__(self, name=None, email=None, password=None):

        self.name = name
        self.email = email
        self.password = password
        
    @staticmethod
    def db_connect():
        credentials = {
            "host": "localhost",
            "user": "root",
            "database": "REACT_REDUX_FLASK_NOTES",
            "password": "Wagvl1chorchana123"
        }
        try:
            connection = myconnect.connect(**credentials)
            return connection
        except:

            return "problem from db server"

    def register(self):
        try:
            conn = self.db_connect()
            if conn != "problem from db server":
                cursor = conn.cursor()
                cursor.execute("""INSERT INTO register(name, email, password) 
                                VALUES
                                (%s, %s, %s)""",(self.name, self.email, self.password))
                conn.commit()
                conn.close()
                return "Successful registration"
            else:
                return "problem from db server"
        except:

            return "Email has already been used"

        
class Database:
    def __init__(self, email, password):

        self.email = email
        self.password = password

    @staticmethod
    def db_connect():
        credentials = {
            "host": "localhost",
            "user": "root",
            "database": "REACT_REDUX_FLASK_NOTES",
            "password": "Wagvl1chorchana123"
        }
        try:
            connection = myconnect.connect(**credentials)
            return connection
        except:

            return "problem from db server"
        
    def loggin(self):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT name, email, password FROM register
                        WHERE email = %s """,(self.email,))
        data = cursor.fetchone()
        
        conn.close()

        return data
    

class Note_Db:
    def __init__(self, email = None, note= None, time= None, important= None):
        self.email = email
        self.note = note
        self.time = time
        self.important = important 
        

    @staticmethod
    def db_connect():
        credentials = {
            "host": "localhost",
            "user": "root",
            "database": "REACT_REDUX_FLASK_NOTES",
            "password": "Wagvl1chorchana123"
        }
        try:
            connection = myconnect.connect(**credentials)
            return connection
        except:

            return "problem from db server"
    
    def add_note(self):
        conn = self.db_connect()
        cursor = conn.cursor()
        
        _SQL = ("""INSERT INTO notes(user_email, note, insert_time, important) 
                                        VALUES (%s, %s, %s, %s)
                                        """)
        values = (self.email, self.note, self.time, self.important)
        cursor.execute(_SQL, values)
                
        conn.commit()
        conn.close()
    
    def del_note(self):
        conn = self.db_connect()
        cursor = conn.cursor()
        _SQL = ("""DELETE FROM notes
                WHERE user_email = %s and insert_time = %s""")
                                                     
        values = (self.email, self.time)
        cursor.execute(_SQL, values)
        
        conn.commit()
        conn.close()

    def update_inp_cont(self, time, email, condition):
        conn = self.db_connect()
        cursor = conn.cursor()
        if condition == "changeImportant":
            _SQL = ("""UPDATE notes SET insert_time = %s, important = %s
                        WHERE insert_time = %s and user_email = %s and note = %s """)
            values = (self.time, self.important, time, email, self.note )
            cursor.execute(_SQL, values)
        elif condition == "changeContent":
            
            _SQL =("""UPDATE notes SET insert_time = %s, note = %s
                    WHERE insert_time = %s and user_email = %s""")
            values = (self.time, self.note, time, email, )
            cursor.execute(_SQL, values)
            print(self.note)
        conn.commit()
        conn.close()
            
    def get_all(self):
        conn = self.db_connect()
        cursor = conn.cursor()
        cursor.execute("""SELECT * from notes 
                        WHERE user_email = %s""",(self.email,))
        data = cursor.fetchall()

        return data



        
        

        


        
        