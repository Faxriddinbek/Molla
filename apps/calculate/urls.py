from django.urls import path

from apps.calculate.views import calculate_page_views

app_name = 'calculate'


urlpatterns = [
    path('', calculate_page_views, name = 'calculate')
]