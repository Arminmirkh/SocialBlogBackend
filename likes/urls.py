from django.urls import path
from .views import LikeCreateView, LikeDeleteView

urlpatterns = [
    path("posts/<int:post_id>/like/", LikeCreateView.as_view(), name="like-post"),
    path("posts/<int:post_id>/unlike/", LikeDeleteView.as_view(), name="unlike-post"),
]
