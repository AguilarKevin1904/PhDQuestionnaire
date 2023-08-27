from .entities.question import Question

class ModelQuestion():
    @classmethod
    def addQuestion(self, db, question):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO preguntas (question) VALUES (%s)"
            values = (question.newQuestion,)
            cursor.execute(sql, values)
            db.connection.commit()
            data = self.showQuestion(db)
            return data
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def showQuestion(self, db):
            cursor = db.connection.cursor()
            sql = cursor.execute('SELECT DISTINCT question FROM preguntas')
            data = cursor.fetchall()
            cursor.close()
            return data