
from rest_framework import serializers
from .models import Post, Category
from django.contrib.auth import get_user_model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]
class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "author", "category", "created_at", "image"]
class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
            "category",
            "image",
            "created_at",
            "updated_at",
        ]
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "image"]

    def create(self, validated_data):
        request = self.context["request"]
        return Post.objects.create(author=request.user, **validated_data)

