from django.db import models


class Company(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(null=False, blank=False, default=' ')
    contact = models.CharField(null=True, max_length=1024)
    address = models.CharField(null=False, max_length=512)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    content = models.TextField(null=False, max_length=1024)
    types = models.BooleanField(default=0)
    start = models.DateField()
    end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'