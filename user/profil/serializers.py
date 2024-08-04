from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    follower = UserProfileSerializer()
    following = UserProfileSerializer()
    class Meta:
        model = Follow
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user_name = UserProfileSerializer()
    class Meta:
        model = Post
        fields = ['user_name', 'image', 'video', 'caption', 'hashtag']


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    user = UserProfileSerializer()
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', 'created_at', 'parent', 'like']