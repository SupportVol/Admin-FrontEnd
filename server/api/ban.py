from server import *


class Ban:
    def __init__(self, user_id, uid):
        self.user_id = user_id
        self.headers = {"uid": uid}
        self.url = BASE_URL + "/api/ban"

    def is_user_banned(self):
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
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "banUID": self.user_id,
            },
        ).json()
        return response["response"][1]

    def un_ban_user(self):
        response = requests.put(
            self.url,
            headers=self.headers,
            json={
                "banUID": self.user_id,
            },
        ).json()
        return response["response"][1]

    def get_all_users(self):
        response = requests.get(BASE_URL + "/api/auth/all", headers=self.headers)
        response = response.json()
        return response["response"][1]
