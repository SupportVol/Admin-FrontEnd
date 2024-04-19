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
            json={"all": getAll},
        ).json()
        return response["response"][1]

    def approve(
        self,
    ):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
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

    def decline(
        self,
    ):
        response = requests.put(
            self.url,
            headers=self.headers,
            json={
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
