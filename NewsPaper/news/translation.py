from .models import Category, Post
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Post)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('post_type', 'title', 'post_content',)

