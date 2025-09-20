from django.urls import path

from apps.bloc.views import BlogListView, home_page_views, page_views_404, blog_detail_views, cart_page_views, checkout_page_views, dashboard_page_views, faq_page_views, wishlist_page_views, BlogDetailView, pages_about_views
app_name = 'bloc'

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name = 'blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name = 'detail'),
    path('', home_page_views, name = 'home'),
    path('404/', page_views_404, name = '404'),
    path('blog-detail', blog_detail_views, name = 'detail'),
    path('cart/', cart_page_views, name = 'cart'),
    path('checkout/', checkout_page_views, name = 'checkout'),
    path('dashboard/', dashboard_page_views, name = 'dashboard'),
    path('faq/', faq_page_views, name = 'faq'),
    path('wishlist/', wishlist_page_views, name = 'wishlist'),
    path('about/', pages_about_views, name = 'about'),
]