from rest_framework import serializers

from commentApp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, instance, **validated_data):
        instance['user'] = self.fields["user"].get_default()
        return super().create(instance)
