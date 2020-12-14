from django.contrib import admin
from .models import Novelty, Category


class NoveltyRedactor(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published','category')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('created_at', 'category')


class CategoryRedactor(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Novelty, NoveltyRedactor)
admin.site.register(Category, CategoryRedactor)
