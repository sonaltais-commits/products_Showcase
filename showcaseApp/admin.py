from django.contrib import admin
from .models import Category, Project


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'media_type', 'created_at')
    list_filter = ('category', 'media_type')
    search_fields = ('title', 'tagline')