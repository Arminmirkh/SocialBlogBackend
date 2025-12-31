from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Like
from posts.models import Post
from .serializers import LikeCreateSerializer

class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = Post.objects.get(id=post_id)
        serializer.save(user=self.request.user, post=post)

class LikeDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        post_id = self.kwargs.get("post_id")
        post = Post.objects.get(id=post_id)
        return Like.objects.get(post=post, user=self.request.user)
