from flask import render_template, request

from . import app


@app.errorhandler(404)
def page_not_fonud(error):
  if request.path.startswith('/assets/') or request.path.startswith('/ar/assets/'):
     return "404 file not found", 404
  return render_template('errors/404.html' if request.path[:4] != "/ar/" else 'errors/ar-404.html',  title="404 error"), 404


@app.errorhandler(500)
def server_error(error):
  return render_template('errors/500.html' if request.path[:4] != "/ar/" else 'errors/ar-500.html',  title="500 error"), 500