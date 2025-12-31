from django.urls import path
from .views import CommentListCreateView, ReplyCreateView

urlpatterns = [
    path("posts/<int:post_id>/comments/", CommentListCreateView.as_view(), name="comments"),
    path("comments/<int:parent_id>/reply/", ReplyCreateView.as_view(), name="comment-reply"),
]
