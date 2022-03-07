from users.db import db
import uuid



class Post:

    def __init__(self, email, content) -> None:
        self.email = email
        self.content = content

    

    def create_post(self):

        # create user obj

        post = {
            "_id" : uuid.uuid4().hex,
            "email" : self.email ,
            "content":self.content
        }
    
        return db.posts.insert_one(post)




