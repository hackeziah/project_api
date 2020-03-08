# from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .views import (
    PostList,
    CategoryList
)


urlpatterns = [
    url(r'^$', PostList.as_view(), name='posts'),
    url(r'^categorys$', CategoryList.as_view(), name='categorys')
]
