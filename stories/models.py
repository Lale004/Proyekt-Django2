from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title