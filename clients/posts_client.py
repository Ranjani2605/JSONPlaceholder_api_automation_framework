from clients.base_client import BaseClient
from config import config


class PostsClient(BaseClient):


    def get_all_posts(self):
        return self.get("/posts")

    def get_post_by_id(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create_post(self, payload):
        return self.post("/posts", payload=payload)

    def update_post(self, post_id, payload):
        return self.put("/posts/{post_id}", payload=payload)

    def partially_update_post(self, post_id, payload):
        return self.patch(f"/posts/{post_id}", payload=payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")

    def get_posts_by_user_id(self, user_id):
        return self.get("/posts", params={"userID": user_id})
