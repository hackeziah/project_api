from rest_framework.generics import ListAPIView
from ..models import Post, Category
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework import viewsets

from .serializers import PostSerializer, CategorySerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # def get_queryset(self):
