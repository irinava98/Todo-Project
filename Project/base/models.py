from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(null=True, blank=True)
    contact_info = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"
