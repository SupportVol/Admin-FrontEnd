from server import *


class Authentication:
    @staticmethod
    def login(email: str, password: str) -> bool:
        body = {"email": decode(email), "password": decode(password)}
        response = requests.post(BASE_URL + "/api/auth/login", json=body)
        response_data = response.json()
        if response.status_code == 200 and response_data["response"][0]:
            uid = response_data["response"][1]
            role_level = requests.get(
                BASE_URL + "/api/usr/extradetails",
                headers={"uid": uid},
                json={"apiKey": API_KEY},
            ).json()["response"][1]
            if role_level["role"] == "Admin":
                session["uid"] = uid
                return True
        return False
