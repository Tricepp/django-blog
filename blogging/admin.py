from django.contrib import admin
from blogging.models import Post, Category

from blogging.models import Post
admin.site.register(Post)
admin.site.register(Category)
