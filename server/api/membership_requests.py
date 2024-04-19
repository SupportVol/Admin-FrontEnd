from server import *


class Membership_Requests:
    """
    A class to represent a Membership Request.

    ...

    Attributes
    ----------
    requestID : str
        a formatted string to represent the request ID
    url : str
        a formatted string to represent the url
    headers : dict
        a dictionary to represent the headers

    Methods
    -------
    get(getAll=False):
        Returns the response of the GET request.
    approve():
        Returns the response of the POST request.
    decline():
        Returns the response of the PUT request.
    """

    def __init__(self, uid, requestID=False):
        """
        Constructs all the necessary attributes for the Membership_Requests object.

        Parameters
        ----------
            uid : str
                user ID
            requestID : str
                request ID
        """

        self.requestID = requestID
        self.url = BASE_URL + "/api/organizations/requests"
        self.headers = {"uid": uid}

    def get(self, getAll=False):
        """
        Sends a GET request and returns the response.

        Parameters
        ----------
            getAll : bool, optional
                a flag to get all (default is False)

        Returns
        -------
            dict
                response of the GET request
        """

        response = requests.get(
            self.url,
            headers=self.headers,
            json={"all": getAll},
        ).json()
        return response["response"][1]

    def approve(self):
        """
        Sends a POST request and returns the response.

        Returns
        -------
            dict
                response of the POST request
        """

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

    def decline(self):
        """
        Sends a PUT request and returns the response.

        Returns
        -------
            dict
                response of the PUT request
        """

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
