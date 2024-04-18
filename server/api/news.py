from server import *


class News:
    def __init__(self, uid, newsID=False):
        self.newsID = newsID
        self.url = BASE_URL + "/api/news"
        self.headers = {"uid": uid}

    def get(self, getAll=False):
        response = requests.get(
            self.url,
            headers=self.headers,
            json={"apiKey": API_KEY, "all": getAll},
        ).json()
        print(response)
        return response["response"][1]

    def create(self, title, description, tags, senderUID, communityID):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "apiKey": API_KEY,
                "newsID": self.newsID,
                "title": title,
                "description": description,
                "tags": tags,
                "senderUID": senderUID,
                "communityID": communityID,
            },
        ).json()
        print(response)
        return response["response"][1]

    def update(self, newsID, title, description, tags, senderUID, communityID):
        response = requests.put(
            self.url,
            headers=self.headers,
            json={
                "apiKey": API_KEY,
                "newsID": self.newsID,
                "title": title,
                "description": description,
                "tags": tags,
                "senderUID": senderUID,
                "communityID": communityID,
            },
        ).json()
        print(response)
        return response["response"][1]

    def delete(self):
        response = requests.delete(
            self.url,
            headers=self.headers,
            json={"apiKey": api_key, "newsID": self.newsID},
        ).json()
        print(response)
        return response["response"][1]
