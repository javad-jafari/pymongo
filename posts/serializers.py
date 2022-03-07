from rest_framework import serializers
from posts.post.models import Post

class PostSerializer(serializers.Serializer):

    email = serializers.EmailField()
    content = serializers.CharField()

    def create(self, validated_data):
        """
        create user ; email as username and make hash password
        """
        email = validated_data.pop("email")
        content = validated_data.pop("content")
        post = Post(email , content)
        obj = post.create_post()
        
        return obj