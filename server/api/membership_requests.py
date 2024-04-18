from server import *


class Membership_Requests:
    def __init__(self, uid, requestID=False):
        self.requestID = requestID
        self.url = BASE_URL + "/api/organizations/requests"
        self.headers = {"uid": uid}

    def get(self, getAll=False):
        response = requests.get(
            self.url,
            headers=self.headers,
            json={"apiKey": API_KEY, "all": getAll},
        ).json()
        print(response)
        return response["response"][1]

    def create(
        self,
        registrationCertificateUrl,
        annualReportUrl,
        legalDocumentsUrl,
        name,
        email,
        password,
        description,
    ):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "apiKey": API_KEY,
                "registrationCertificateUrl": registrationCertificateUrl,
                "annualReportUrl": annualReportUrl,
                "legalDocumentsUrl": legalDocumentsUrl,
                "name": name,
                "email": email,
                "password": password,
                "description": description,
                "requestID": self.requestID,
            },
        ).json()
        print(response)
        return response["response"][1]

    def update(
        self,
        registrationCertificateUrl,
        annualReportUrl,
        legalDocumentsUrl,
        name,
        email,
        password,
        description,
    ):
        response = requests.put(
            self.url,
            headers=self.headers,
            json={
                "apiKey": API_KEY,
                "registrationCertificateUrl": registrationCertificateUrl,
                "annualReportUrl": annualReportUrl,
                "legalDocumentsUrl": legalDocumentsUrl,
                "name": name,
                "email": email,
                "password": password,
                "description": description,
                "requestID": self.requestID,
            },
        ).json()
        print(response)
        return response["response"][1]

    def delete(self):
        response = requests.delete(
            self.url,
            headers=self.headers,
            json={"apiKey": API_KEY, "requestID": self.requestID},
        ).json()
        print(response)
        return response["response"][1]
