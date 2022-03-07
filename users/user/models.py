from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from passlib.handlers.django import django_pbkdf2_sha256
from users.db import db
import uuid
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class User:

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

    

    def signup(self):

        # create user obj

        user = {
            "_id" : uuid.uuid4().hex,
            "email" : self.email ,
            "password":self.password

        }

        # encrypt password
        user["password"] = make_password(user["password"])

        # check exist user

        if db.users.find_one({"email":user["email"]}):
            return Response(status=HTTP_400_BAD_REQUEST)
        
        if db.users.insert_one(user):
            return Response(status=HTTP_201_CREATED)

    
        return Response(status=HTTP_400_BAD_REQUEST)



