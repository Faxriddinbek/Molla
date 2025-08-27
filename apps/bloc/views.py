from django.shortcuts import render

def about_page_views(request):
    return render(request, 'blog-list.html')


def home_page_views(request):
    return render(request, 'home.html')

def page_views_404(request):
    return render(request, '404.html')

def blog_detail_views(request):
    return render(request, 'blog-detail.html')

def cart_page_views(request):
    return render(request, 'cart.html')

def category_page_views(request):
    return render(request, 'category.html')

def checkout_page_views(request):
    return render(request, 'checkout.html')

# def contact_page_views(request):
#     return render(request, 'contact.html')

def dashboard_page_views(request):
    return render(request, 'dashboard.html')

def faq_page_views(request):
    return render(request, 'faq.html')

def login_page_views(request):
    return render(request, 'login.html')

def product_det_page_views(request):
    return render(request, 'product-detail.html')

def wishlist_page_views(request):
    return render(request, 'wishlist.html')