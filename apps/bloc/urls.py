from django.urls import path

from apps.bloc.views import about_page_views, home_page_views, page_views_404, blog_detail_views, cart_page_views,  category_page_views, checkout_page_views, dashboard_page_views, faq_page_views, login_page_views, product_det_page_views, wishlist_page_views

app_name = 'home'

urlpatterns = [
    path('blogs/', about_page_views, name = 'about'),
    path('home/', home_page_views, name = 'home'),
    path('404/', page_views_404, name = '404'),
    path('blog-detail', blog_detail_views, name = 'detail'),
    path('cart/', cart_page_views, name = 'cart'),
    path('category/', category_page_views, name = 'category'),
    path('checkout/', checkout_page_views, name = 'checkout'),
    # path('contact/', contact_page_views, name = 'contact'),
    path('dashboard/', dashboard_page_views, name = 'dashboard'),
    path('faq/', faq_page_views, name = 'faq'),
    path('login/', login_page_views, name = 'login'),
    path('product_d/', product_det_page_views, name = 'product_det'),
    path('wishlist/', wishlist_page_views, name = 'wishlist'),
]