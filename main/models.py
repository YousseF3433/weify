from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Date
from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

class User(db.Model,  UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(18), nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
      return f"<{self.username}, {self.email}, {self.password}>"

class Por(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  filter = db.Column(db.String(30))
  title = db.Column(db.String(80), nullable=False)
  img_src = db.Column(db.String(60))
  url = db.Column(db.String(50), nullable=False)

  def __repr__(self):
    return f"<{self.title}, {self.img_src}, {self.url}>"

class Cat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable=False)
  value = db.Column(db.String(80), nullable=False)

  def __repr__(self):
    return f"<{self.name}, {self.value}>"

class Blog(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), nullable=False)
  description = db.Column(db.Text, nullable=False)
  ar_description = db.Column(db.Text)
  shor_description = db.Column(db.String(180))
  photo = db.Column(db.String(100), nullable=False)
  index = db.Column(db.Integer)
  date = db.Column(Date, default=datetime.now().date())

  def __repr__(self):
    return f"<{self.title}, {self.description}>"
    
class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  quesion = db.Column(db.String(100), nullable=False)
  answer = db.Column(db.String(500), nullable=False)
  
  def __repr__(self):
    return f"<{self.answer}, {self.quesion}>"

class Buying(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  phone = db.Column(db.String(24), nullable=False)
  company = db.Column(db.String(64), nullable=False)
  budget = db.Column(db.String(64), nullable=False)
  name =  db.Column(db.String(24), nullable=False)
  mes = db.Column(db.Text, nullable=False)
  date = db.Column(Date, default=datetime.now().date())

  def __repr__(self):
    return f"<{self.phone}, {self.name}>"

class From(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  from_site = db.Column(db.String(40))
  number = db.Column(db.Integer, default=0)
  site_name = db.Column(db.String(100))
  
  def __repr__(self):
    return f"<{self.id}, {self.from_site}, {self.number}>"
