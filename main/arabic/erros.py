from flask import render_template

from . import ar_bp

@ar_bp.errorhandler(404)
def page_not_fonud_ar(error):
  return "hi" #render_template('errors/ar-404.html',  title="404 error"), 404


@ar_bp.errorhandler(500)
def server_error_ar(error):
  return render_template('errors/ar-500.html',  title="500 error"), 500