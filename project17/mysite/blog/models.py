from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=512)
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approve_comments=True)
    
    def __str__(self):
        return self.title
    
class comments(models.Model):
    post = models.ForeignKey("blog.Post", related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=512)
    created_date = models.DateTimeField(default=timezone.now())