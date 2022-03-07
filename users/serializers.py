from rest_framework import serializers
from users.user.models import User

class UserSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)
    confirm_password = serializers.CharField(max_length=255, write_only=True)

    def create(self, validated_data):
        """
        create user ; email as username and make hash password
        """
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        user = User(email , password)
        obj = user.signup()
        
        return obj

    def validate(self,data):

        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password confirme is incorrect")

        if len(data["password"]) < 5:
            raise serializers.ValidationError("password len must be bigger than 5")
        return data