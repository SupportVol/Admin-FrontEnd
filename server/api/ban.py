from server import *


class Ban:
    """
    A class to represent a Ban.

    ...

    Attributes
    ----------
    user_id : str
        a formatted string to represent the user id
    headers : dict
        a dictionary to represent the headers
    url : str
        a formatted string to represent the url

    Methods
    -------
    is_user_banned():
        Checks if a user is banned.
    ban_user():
        Bans a user.
    un_ban_user():
        Unbans a user.
    get_all_users():
        Gets all users.
    """

    def __init__(self, user_id, uid):
        """
        Constructs all the necessary attributes for the Ban object.

        Parameters
        ----------
            user_id : str
                user's id
            uid : str
                unique identifier
        """
        self.user_id = user_id
        self.headers = {"uid": uid}
        self.url = BASE_URL + "/api/ban"

    def is_user_banned(self):
        """
        Checks if a user is banned.

        Returns
        -------
        bool
            True if user is banned, False otherwise
        """
        response = requests.get(
            self.url,
            headers=self.headers,
            json={
                "banUID": self.user_id,
            },
        ).json()
        print(response)
        return response["response"][1]

    def ban_user(self):
        """
        Bans a user.

        Returns
        -------
        str
            response after banning a user
        """
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "banUID": self.user_id,
            },
        ).json()
        return response["response"][1]

    def un_ban_user(self):
        """
        Unbans a user.

        Returns
        -------
        str
            response after unbanning a user
        """
        response = requests.put(
            self.url,
            headers=self.headers,
            json={
                "banUID": self.user_id,
            },
        ).json()
        return response["response"][1]

    def get_all_users(self):
        """
        Gets all users.

        Returns
        -------
        list
            a list of all users
        """
        response = requests.get(BASE_URL + "/api/auth/all", headers=self.headers)
        response = response.json()
        return response["response"][1]
