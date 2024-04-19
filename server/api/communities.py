from server import *

# Importing all modules from server


class Communities(CRUD_Requests):
    """
    Communities class that inherits from CRUD_Requests.
    This class is used to manage communities.
    """

    def __init__(self, community_uid, uid):
        """
        Initialize Communities instance.

        Args:
            community_uid (str): The unique identifier for the community.
            uid (str): The unique identifier for the user.
        """
        super().__init__(uid, community_uid, "/api/community")


# Below is an example of the data structure that this class might work with:
# {
#     "apiKey": API_KEY,  # The API key for authentication
#     "name": name,  # The name of the community
#     "title": title,  # The title of the community
#     "description": description,  # A description of the community
#     "photoUrl": photoUrl,  # A URL to a photo representing the community
#     "banner": banner,  # A banner image for the community
#     "theme": theme,  # The theme of the community
#     "members": members,  # A list of members in the community
# }
