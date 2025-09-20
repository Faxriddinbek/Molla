from django.urls import path
from .views import ProductDetailView, ProductsListView
app_name = 'product'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('', ProductsListView.as_view(), name='list'),
]