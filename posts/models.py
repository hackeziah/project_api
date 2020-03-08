from django.db import models


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
