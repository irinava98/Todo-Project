from django.contrib import admin
from .models import Task, Category, Tag, UserProfile

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(UserProfile)
