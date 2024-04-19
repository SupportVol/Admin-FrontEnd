from server import *


class Communities(CRUD_Requests):
    def __init__(self, community_uid, uid):
        super().__init__(uid, community_uid, "/api/community")

# {
#     "apiKey": API_KEY,
#     "name": name,
#     "title": title,
#     "description": description,
#     "photoUrl": photoUrl,
#     "banner": banner,
#     "theme": theme,
#     "members": members,
# }
