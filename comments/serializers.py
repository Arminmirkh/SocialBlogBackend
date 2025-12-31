from rest_framework import serializers
from .models import Comment

class RecursiveCommentSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = CommentSerializer(value, context=self.context)
        return serializer.data
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    replies = RecursiveCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "content",
            "created_at",
            "updated_at",
            "parent",
            "replies",
        ]
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "parent"]

    def create(self, validated_data):
        post = self.context["post"]     # از view
        user = self.context["request"].user

        return Comment.objects.create(
            author=user,
            post=post,
            **validated_data
        )
class ReplyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]

    def create(self, validated_data):
        parent = self.context["parent"]
        user = self.context["request"].user
        post = parent.post

        return Comment.objects.create(
            author=user,
            post=post,
            parent=parent,
            **validated_data
        )


