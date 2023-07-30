from .entities.User import User

class ModelUser():
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, fullname, email, password FROM usuarios
                    WHERE fullname = '{}'""".format(user.fullname)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], User.check_password(row[3], user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, fullname, email FROM usuarios WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def registerUser(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO usuarios (fullname, email, password) VALUES (%s, %s, %s)"
            values = (user.fullname, user.email, user.password)
            cursor.execute(sql, values)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)