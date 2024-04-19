"""
this has all of imports and other init configs and other main
"""

from flask import *
import requests


app = Flask(__name__)  # init flask app
app.debug = True
app.secret_key = "SupportVol"  # secret key
# BASE_URL = "http://localhost:3000"
BASE_URL = "https://supportvol-dot-support-vol.as.r.appspot.com"
API_KEY = "VzruLfssZ17zQzGsVnlH"
from server.help_funcs import *
from server.api import *
from server.routes import *
