from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=(
            Follow._meta.get_field('following')
            .remote_field.model.objects.all()
        )
    )

    class Meta:
        model = Follow
        fields = '__all__'

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']

        if user == following:
            raise serializers.ValidationError('Нельзя подписаться на себя')

        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError('Подписка уже существует')

        return data
