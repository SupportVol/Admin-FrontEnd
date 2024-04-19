import base64
import smtplib
import datetime
from email.mime.text import MIMEText
from server import *

"""
This file contains utility functions and classes used throughout the application.
"""


class CRUD_Requests:
    """
    Class to handle CRUD operations.
    """

    def __init__(self, uid, uniqueID=False, endpoint="/api/news"):
        """
        Initialize CRUD_Requests with uid, uniqueID and endpoint.
        """
        self.uniqueID = uniqueID
        self.url = BASE_URL + endpoint
        self.headers = {"uid": uid}

    def get(self, get_all=False):
        """
        Get request to the server.
        """
        response = requests.get(
            self.url,
            headers=self.headers,
            json={"apiKey": API_KEY, "all": get_all},
        ).json()
        return response["response"][1]

    def create(self, **kwargs):
        """
        Create request to the server.
        """
        response = requests.post(
            self.url,
            headers=self.headers,
            json={"apiKey": API_KEY, **kwargs},
        ).json()
        print(response)
        return response["response"][1]

    def update(self, **kwargs):
        """
        Update request to the server.
        """
        response = requests.put(
            self.url,
            headers=self.headers,
            json={"apiKey": API_KEY, **kwargs},
        ).json()
        print(response)
        return response["response"][1]

    def delete(self, uniqueName):
        """
        Delete request to the server.
        """
        response = requests.delete(
            self.url,
            headers=self.headers,
            json={"apiKey": API_KEY, "uniqueName": self.uniqueID},
        ).json()
        print(response)
        return response["response"][1]


def encode(message: str) -> bytes:
    """
    Encode a string for privacy and encryption.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64encode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def decode(message: str) -> bytes:
    """
    Decode a string for privacy and encryption.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64decode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def login_verification():
    """
    Verify if the user is logged in.
    """
    return "uid" in session
