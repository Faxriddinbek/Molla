from django.urls import path

from apps.acount.views import contact_page_views

app_name = 'home'

urlpatterns = [
    path('contact_t', contact_page_views, name = 'contact')
]