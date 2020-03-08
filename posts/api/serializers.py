from rest_framework import serializers
from ..models import Post, Category
from rest_framework.serializers import ModelSerializer


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'status',
            'created_by',
            'date_posted',
            'category'
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]
