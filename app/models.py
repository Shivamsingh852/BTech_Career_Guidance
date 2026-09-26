from . import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    
    # Profile Data (Module 1)
    academic_percentage = db.Column(db.Float, nullable=True)
    programming_skill = db.Column(db.Integer, nullable=True) # 1-10
    communication_skill = db.Column(db.Integer, nullable=True) # 1-10
    analytical_skill = db.Column(db.Integer, nullable=True) # 1-10
    interests = db.Column(db.String(300), nullable=True)
    personality_type = db.Column(db.String(50), nullable=True) # e.g., Introvert/Extrovert


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    predicted_career = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False) # 1 to 5
    comments = db.Column(db.Text, nullable=True)
    user = db.relationship('User', backref=db.backref('feedbacks', lazy=True))
