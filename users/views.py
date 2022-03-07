from rest_framework.views import APIView
from users.serializers import UserSerializer
from rest_framework.response import Response
from users.db import db
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class UserAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):

        ser = UserSerializer(db.users.find(), many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        ser = UserSerializer(data=request.data)

        if ser.is_valid():
            ser.save()
            return Response({"user":request.data},status=HTTP_201_CREATED)
        return Response({"error":ser.errors},status=HTTP_400_BAD_REQUEST)