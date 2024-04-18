from server import *


class Api_Key:
    def __init__(self, uid):
        self.url = BASE_URL + "/api/keys"
        self.headers = {"uid": uid}

    def get_all(self):
        response = requests.get(
            self.url, headers=self.headers, json={"apiKey": API_KEY}
        ).json()
        return response["response"][1]

    def create(self, owner_name, owner_uid, owner_email):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "apiKey": API_KEY,
                "ownerName": owner_name,
                "ownerUid": owner_uid,
                "ownerEmail": owner_email,
            },
        ).json()
        print(response)
        return response["response"][1]

    def update(self, owner_name, owner_uid, owner_email):
        response = requests.put(
            self.url,
            headers=self.headers,
            json={
                "apiKey": API_KEY,
                "ownerName": owner_name,
                "ownerUid": owner_uid,
                "ownerEmail": owner_email,
            },
        ).json()
        print(response)
        return response["response"][1]

    def delete(self, api_key):
        response = requests.delete(
            self.url, headers=self.headers, json={"apiKey": api_key}
        ).json()
        print(response)
        return response["response"][1]

    def get_one(self):
        response = requests.get(
            self.url, headers=self.headers, json={"apiKey": API_KEY, "all": False}
        ).json()
        print(response)
        return response[1]
