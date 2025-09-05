from django.shortcuts import render, get_object_or_404
from datetime import timedelta
from django.db.models import Count
from django.utils import timezone
from .models import BlogModel, BlogCategoryModel, BlogTagModel, BlogViewModel


def about_page_views(request):
    blogs = BlogModel.objects.filter(
        status=BlogModel.BlogStatus.PUBLISHED
    )
    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()
    most_popular_blogs = (
        BlogModel.objects
        .annotate(views_count=Count('views', distinct=True))
        .order_by('-views_count')[:4]
    )

    context = {
        "blogs": blogs,
        "categories": categories,
        "tags": tags,
        "most_popular_blogs": most_popular_blogs,
    }
    return render(
        request, 'blog-list.html',
        context
    )


def check_blog_view(request, blog):
    # Get user IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        user_ip = x_forwarded_for.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')

    # Find last view of this blog by this IP
    last_view = BlogViewModel.objects.filter(
        user_ip=user_ip, blog=blog
    ).order_by('-created_at').first()

    # If never viewed OR last view was more than 7 days ago → create new record
    if not last_view or (timezone.now() - last_view.created_at) > timedelta(minutes=1):
        BlogViewModel.objects.create(user_ip=user_ip, blog=blog)



def blog_detail(request, pk):
    blog = get_object_or_404(BlogModel, id=pk)
    check_blog_view(request, blog)

    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()

    # related blogs by same categories
    related_blogs = BlogModel.objects.filter(
        category__in=blog.category.all()
    ).exclude(id=blog.id).distinct()

    most_popular_blogs = (
        BlogModel.objects
        .annotate(views_count=Count('views__user_ip', distinct=True))
        .order_by('-views_count')[:4]
    )

    context = {
        "blog": blog,
        "categories": categories,
        "tags": tags,
        "related_blogs": related_blogs,
        "most_popular_blogs": most_popular_blogs,
    }
    return render(request, 'blog-detail.html', context)

def home_page_views(request):
    return render(request, 'home.html')

def page_views_404(request):
    return render(request, '404.html')

def blog_detail_views(request):
    return render(request, 'blog-detail.html')

def cart_page_views(request):
    return render(request, 'cart.html')

def product_page_views(request):
    return render(request, 'products.html')

def checkout_page_views(request):
    return render(request, 'checkout.html')

def contact_page_views(request):
    return render(request, 'contact.html')

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


def pages_about_views(request):
    return render(request, 'about.html')