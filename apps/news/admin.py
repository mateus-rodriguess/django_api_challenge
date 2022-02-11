from django.contrib import admin

from .models import Articles, Category, Author


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass