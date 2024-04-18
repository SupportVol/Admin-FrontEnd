from server import *


class Communities:
    def __init__(self, community_uid, uid):
        self.community_uid = community_uid
        self.url = BASE_URL + "/api/community"
        self.headers = {"uid": uid}

    def get(self, display_all=False):
        response = requests.get(
            self.url,
            headers=self.headers,
            json={
                "communityuid": self.community_uid,
                "apiKey": API_KEY,
                "all": display_all,
            },
        ).json()
        print(response)
        return response["response"][1]

    def create(self, name: str, title, description, photoUrl, banner, theme, members):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "apiKey": API_KEY,
                "name": name,
                "title": title,
                "description": description,
                "photoUrl": photoUrl,
                "banner": banner,
                "theme": theme,
                "members": members,
            },
        ).json()
        print(response)
        return response["response"][1]

    def update(self, name, title, description, photoUrl, banner, theme, members):
        response = requests.put(
            self.url,
            headers=self.headers,
            json={
                "apiKey": API_KEY,
                "name": name,
                "title": title,
                "description": description,
                "photoUrl": photoUrl,
                "banner": banner,
                "theme": theme,
                "members": members,
            },
        ).json()
        print(response)
        return response["response"][1]

    def delete(self):
        response = requests.delete(
            self.url,
            headers=self.headers,
            json={"apiKey": API_KEY, "community_uid": self.community_uid},
        ).json()
        print(response)
        return response["response"][1]
