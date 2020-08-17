from db import db

class Tema(db.Model):
    id_tema = db.Column(db.Integer, primary_key=True)
    tema = db.Column(db.String)
    tema_certo = db.Column(db.String)

    def __init__(self, tema, tema_certo):
        self.tema = tema
        self.tema_certo = tema_certo

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Subtemas(db.Model):
    __tablename__ = 'subtema'
    id_subtema = db.Column(db.Integer, primary_key=True)
    tema = db.Column(db.String)
    subtema = db.Column(db.String)

    def __init__(self, tema, subtema):
        self.tema = tema
        self.subtema = subtema

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        


