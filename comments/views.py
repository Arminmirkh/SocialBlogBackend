from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer
from posts.models import Post

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return Comment.objects.filter(post__id=post_id, parent=None)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)

# Reply to comment
class ReplyCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        parent_id = self.kwargs.get("parent_id")
        parent = Comment.objects.get(id=parent_id)
        serializer.save(author=self.request.user, post=parent.post, parent=parent)
