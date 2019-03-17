from django.contrib import admin
from .models import Article, Tag


# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'date']


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    pass
