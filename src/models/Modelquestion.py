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
        except Exception as ex:
            raise Exception(ex)