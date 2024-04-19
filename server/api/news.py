from server import *

# Importing necessary modules from server


# Creating a News class which inherits from CRUD_Requests
class News(CRUD_Requests):
    """
    News class for handling news related CRUD requests.

    Attributes:
        uid (str): User ID
        newsID (bool): News ID. Default is False.
    """

    def __init__(self, uid, newsID=False):
        """
        The constructor for News class.

        Parameters:
            uid (str): User ID
            newsID (bool): News ID. Default is False.
        """
        # Call to the parent class constructor
        super().__init__(uid, newsID, "/api/news")


# Below is a sample dictionary structure that can be used with this class
# {
#     "newsID": self.newsID,
#     "title": title,
#     "description": description,
#     "tags": tags,
#     "senderUID": senderUID,
#     "communityID": communityID,
# }
