from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = ["id", "user", "created_at"]
class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = []  

    def create(self, validated_data):
        user = self.context["request"].user
        post = self.context["post"]

        like, created = Like.objects.get_or_create(
            user=user,
            post=post
        )
        return like
