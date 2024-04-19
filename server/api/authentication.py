from server import *


class Authentication:
    """
    This class provides methods for user authentication.
    """

    @staticmethod
    def login(email: str, password: str) -> bool:
        """
        This method logs in a user with the provided email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        # Prepare the request body
        body = {"email": decode(email), "password": decode(password)}

        # Send a POST request to the login API
        response = requests.post(BASE_URL + "/api/auth/login", json=body)

        # Parse the response
        response_data = response.json()

        # Check if the response is successful and the user is authenticated
        if response.status_code == 200 and response_data["response"][0]:
            uid = response_data["response"][1]

            # Get the role level of the user
            role_level_response = requests.get(
                BASE_URL + "/api/usr/extradetails",
                headers={"uid": uid},
            )

            # Print the role level response for debugging
            print(role_level_response)
            print(role_level_response.json())

            # Parse the role level response
            role_level = role_level_response.json()

            # Check if the user is an admin
            if role_level["role"] == "Admin":
                # Store the user id in the session
                session["uid"] = uid

                # Return True indicating that the login is successful
                return True

        # Return False indicating that the login is unsuccessful
        return False
