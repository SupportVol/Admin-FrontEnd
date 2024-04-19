"""
this has all of imports and other init configs and other main
"""

from flask import *
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


app = Flask(__name__)  # init flask app
app.debug = True
app.secret_key = "SupportVol"  # secret key
# BASE_URL = "http://localhost:3000"
BASE_URL = "https://supportvol-dot-support-vol.as.r.appspot.com"
API_KEY = "VzruLfssZ17zQzGsVnlH"
req_session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
req_session.mount("http://", adapter)
req_session.mount("https://", adapter)
from server.help_funcs import *
from server.api import *
from server.routes import *
