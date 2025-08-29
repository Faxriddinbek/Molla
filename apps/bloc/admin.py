from django.contrib import admin

# from apps.bloc.models import BlogAuthor, BlogModel, CommentModel
from  apps.bloc.models import BlocAuthorModel, BlocCategoryModel, BlocTagModel, BlogsModel, BlogComentaryModel

admin.site.register(BlocAuthorModel)
admin.site.register(BlocCategoryModel)
admin.site.register(BlocTagModel)
admin.site.register(BlogsModel)
admin.site.register(BlogComentaryModel)
