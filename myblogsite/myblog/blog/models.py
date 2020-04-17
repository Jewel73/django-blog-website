from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, null = True)

    def __str__(self):
        return self.category_name

class Tag(models.Model):
    tags_name = models.CharField(max_length=100, null= True)

    def __str__(self):
        return self.tags_name

class Post(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200, null = True, blank=True)
    post_image = models.ImageField(null= True, blank= True)
    post_content = models.TextField()
    post_category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    post_tags = models.ManyToManyField(Tag)
    post_created = models.DateTimeField(auto_now_add=True, null= True)

    class Meta:
        ordering =['post_created']

    def __str__(self):
        return self.post_title