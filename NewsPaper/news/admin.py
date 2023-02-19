from django.contrib import admin
from .models import Post, PostCategory, Category
from modeltranslation.admin import TranslationAdmin

class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Category)
