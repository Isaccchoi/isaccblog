from django.contrib import admin

# Register your models here.

from .models import Category
from .models import Post
from .models import Comment
from .models import Tag



class PostAdmin(admin.ModelAdmin):
    field = ('category', 'title', 'content', 'tags', 'active')
    models = Post
    list_display = ('category', 'title', 'active')

admin.site.register(Post, PostAdmin)


admin.site.register(Category)

admin.site.register(Tag)

admin.site.register(Comment)
