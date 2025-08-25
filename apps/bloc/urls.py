from django.urls import path

from apps.bloc.views import about_page_views, home_page_views

app_name = 'bloc'

urlpatterns = [
    path('', about_page_views, name = 'about'),
    path('', home_page_views, name = 'home')
]