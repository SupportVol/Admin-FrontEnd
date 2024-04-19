from server import *

# Importing all modules from server


# Define a class Api_Key which inherits from CRUD_Requests
class Api_Key(CRUD_Requests):
    """
    This class is used to handle API keys. It inherits from the CRUD_Requests class.
    """

    def __init__(self, change_api_key, uid):
        """
        Initialize the Api_Key object.

        Parameters:
        change_api_key (str): The new API key to be set.
        uid (str): The unique identifier for the user.
        """
        # Call the parent class's constructor
        super().__init__(uid, change_api_key, "/api/keys")


# The following commented code seems to be a sample of the data structure used in this class.
# {
#     "ownerName": owner_name,
#     "ownerUid": owner_uid,
#     "ownerEmail": owner_email,
# }
