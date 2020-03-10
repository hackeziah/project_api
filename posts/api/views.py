from ..models import Post, Category
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.filters import (OrderingFilter)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from .serializers import (
    PostSerializer,
    CategorySerializer,
    PostCreateSerializer
)

# POST


class PostUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticated
    ]

    lookup_field = 'id'


class PostDestroyAPI(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostCreateAPI(generics.CreateAPIView):
    queryset = Post.objects.all()
    perssion_classes = [permissions.IsAuthenticated]
    serializer_class = PostCreateSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [OrderingFilter]

# Category


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # def get_queryset(self):
