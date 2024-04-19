from server import *


class Api_Key(CRUD_Requests):
    def __init__(self, change_api_key, uid):
        super().__init__(uid, change_api_key, "/api/keys")


# {
#     "ownerName": owner_name,
#     "ownerUid": owner_uid,
#     "ownerEmail": owner_email,
# }
