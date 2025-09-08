from django.contrib import admin

from apps.bloc.models import BlogCategoryModel, BlogTagModel, BlocAuthorModel, BlogModel, BlogViewModel



@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', "title")
    search_fields = ['title']
    list_filter = ['created_at']

@admin.register(BlogTagModel)
class BlocTagModelAdmin(admin.ModelAdmin):
    list_display = ('id', "title")
    search_fields = ['title']
    list_filter = ['created_at']

@admin.register(BlocAuthorModel)
class BlogAuthorModelAdmin(admin.ModelAdmin):
    list_display = ('id', "full_name")
    search_fields = ["full_name"]
    list_filter = ['created_at']
    ordering = ["id"]

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('id', "title", 'status' ,'created_at')
    search_fields = ['title', 'content']
    list_filter = ['created_at', 'status']

@admin.register(BlogViewModel)
class BlogViewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_ip', 'blog__title', 'created_at']
    search_fields = ['user_ip']
    list_filter = ['created_at', 'user_ip']