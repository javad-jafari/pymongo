from rest_framework.views import APIView
from posts.serializers import PostSerializer
from rest_framework.response import Response
from users.db import db
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class PostAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):

        ser = PostSerializer(db.posts.find(), many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        ser = PostSerializer(data=request.data)

        if ser.is_valid():
            ser.save()
            return Response({"post":request.data},status=HTTP_201_CREATED)
        return Response({"error":ser.errors},status=HTTP_400_BAD_REQUEST)
