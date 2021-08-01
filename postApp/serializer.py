from rest_framework import serializers
from postApp.models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, instance, **validated_data):
        instance['username'] = self.fields["username"].get_default()
        return super().create(instance)
