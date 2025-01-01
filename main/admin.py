import os
from flask import request, flash
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from main import app, db
from .models import Question, User, Por, Blog, Buying, From, Cat


class MyAdminIndexView(AdminIndexView):
  @expose('/', methods=["GET", "POST"])
  def default_view(self):
    if request.method == "POST":
      if 'file' not in request.files:
          return 'No file part'
      file = request.files['file']
      if file.filename == '':
         return 'No selected file'
      filename = file.filename
      save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename) # type: ignore
      os.makedirs(os.path.dirname(save_path), exist_ok=True)
      file.save(save_path)
      flash(f'img {filename} uploaded successfully!', "info")
    return self.render("admin/admin-index.html")

  def is_accessible(self): 
    return True #current_user.is_authenticated and current_user.is_admin


class UserModelView(ModelView):
    def is_accessible(self): 
        return True #current_user.is_authenticated and current_user.is_admin


class MyModelView(ModelView):
    def is_accessible(self):
        return True #current_user.is_authenticated and current_user.is_admin


admin = Admin(app, template_mode='bootstrap3', index_view=MyAdminIndexView())
admin.add_view(UserModelView(User, db.session))
admin.add_view(MyModelView(Por, db.session))
admin.add_view(MyModelView(Blog, db.session))
admin.add_view(MyModelView(Question, db.session))
admin.add_view(MyModelView(Buying, db.session))
admin.add_view(MyModelView(From, db.session))
admin.add_view(MyModelView(Cat, db.session))