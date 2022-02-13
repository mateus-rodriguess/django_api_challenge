from django.contrib import admin

from .models import Articles, Category, Author


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', "category", "author"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', "created"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', "created", "user_id", "id"]