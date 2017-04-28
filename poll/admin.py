from django.contrib import admin
from poll.models import Post, Document, Article


# Register your models here.
admin.site.register(Post)

admin.site.register(Document)
admin.site.register(Article)
