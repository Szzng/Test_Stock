from django.db import models
from django.contrib.auth.models import User


class Keyword(models.Model):
    keyword = models.CharField(max_length=300, primary_key=True)
    owner = models.ManyToManyField(User)

    def __str__(self):
        return self.keyword


class NewsOfKeyword(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    url = models.URLField()
    written_at = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
