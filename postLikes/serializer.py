from rest_framework import serializers

from postLikes.models import Likes


class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'
