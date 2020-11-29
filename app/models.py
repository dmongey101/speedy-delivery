from app import db, login

@login.user_loader
def load_user(user):
    return User.get(user)


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean())
    last_logged_in = db.Column(db.DateTime())
    modified_on = db.Column(db.DateTime())
    created_on = db.Column(db.DateTime())

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
# class Recipe(db.Model):
#     id = db.Column()