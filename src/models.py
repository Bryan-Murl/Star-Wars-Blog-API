from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import DateTime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class People(db.Model):
    __tablename__ = 'people'
    id  = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    skin_color = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    edited = db.Column(db.DateTime, nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            # do not serialize the password, its a security breach
        }
class Favpeople(db.Model):
    __tablename__ = 'favpeople'
    id= db.Column(db.Integer, primary_key=True)
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    ppeople = db.relationship(People)
    iduser = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    
    def __repr__(self):
        return '<Favpeople %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_people": self.id_people,
            "iduser": self.iduser,
        }
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter= db.Column(db.Integer, nullable=False)
    rotation_period= db.Column(db.Integer, nullable=False)
    orbital_period= db.Column(db.Integer, nullable=False)
    gravity= db.Column(db.String(50), nullable=False)
    population= db.Column(db.Integer, nullable=False)
    climate= db.Column(db.String(50), nullable=False)
    terrain= db.Column(db.String(50), nullable=False)
    surface_water= db.Column(db.Integer, nullable=False)
    created= db.Column(db.DateTime, nullable=False)
    edited= db.Column(db.DateTime, nullable=False)
    url= db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
        }

class Favplanets(db.Model):
    __tablename__ = 'favplanets'
    id= db.Column(db.Integer, primary_key=True)
    idplaneta = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planeta = db.relationship(Planets)
    iduser = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def __repr__(self):
        return '<Favplanets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "idplaneta": self.id_people,
            "iduser": self.iduser,
        }