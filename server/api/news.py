from server import *


class News(CRUD_Requests):
    def __init__(self, uid, newsID=False):
        super().__init__(uid, newsID, "/api/news")


# {
#     "newsID": self.newsID,
#     "title": title,
#     "description": description,
#     "tags": tags,
#     "senderUID": senderUID,
#     "communityID": communityID,
# }
