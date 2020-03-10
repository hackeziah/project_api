# from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import (
    PostList,
    CategoryList,
    PostCreateAPI,
    PostDetailView,
    PostUpdateAPI,
    PostDestroyAPI
)


urlpatterns = [
    url(r'^posts/$', PostList.as_view(), name='posts'),
    url(r'^posts-create$', PostCreateAPI.as_view(), name='post-create'),
    url(r'^posts/(?P<id>\d+)/$', PostDetailView.as_view(), name='posts-details'),
    url(r'^posts/(?P<id>[\w-]+)/edit/$',
        PostUpdateAPI.as_view(), name='posts-edit'),
    url(r'^posts/(?P<id>[\w-]+)/delete$',
        PostDestroyAPI.as_view(), name='posts-detroy'),

    url(r'^categorys$', CategoryList.as_view(), name='categorys')

]
