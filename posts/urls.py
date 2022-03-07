from django.urls import path
from posts.views import PostAPIView



urlpatterns = [
    path('', PostAPIView.as_view(), name="posts")
]
