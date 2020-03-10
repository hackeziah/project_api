from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

# from project_api import settings
# from rest_framework import settings
# from settings import AUTH_USER_MODEL


class Category(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Post(models.Model):
    PUBLISH = 0
    NOT_PUBLISH = 1

    STATUS = (
        (PUBLISH, "Publish"),
        (NOT_PUBLISH, "Not Publish"),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="title", max_length=255)
    content = models.TextField(
        max_length=255, help_text="Type Your Content Here")
    status = models.IntegerField(
        verbose_name="Status", choices=STATUS, default=0)
    created_by = models.CharField(verbose_name="Created By", max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
