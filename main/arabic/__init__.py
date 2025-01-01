from flask import Blueprint

ar_bp = Blueprint('ar', __name__, template_folder='ar-templates', static_folder="../assets")

from .routs import *
from .erros import *