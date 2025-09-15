from django.shortcuts import render, get_object_or_404
from datetime import timedelta
from django.db.models import Count
from django.utils import timezone
from .models import BlogModel, BlogCategoryModel, BlogTagModel, BlogViewModel
from apps.shop.models import ProductCategory, ProductSize, ProductColor, ProductModel, ProductBrand
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
    if not last_view or (timezone.now() - last_view.created_at) > timedelta(days=1):
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
    categories = ProductCategory.objects.all()
    brands = ProductBrand.objects.all()
    colors = ProductColor.objects.all()
    sizes = ProductSize.objects.all()
    products = ProductModel.objects.all()

    cat_id = request.GET.get('cat')
    brand_id = request.GET.get('brand_id')
    color_id = request.GET.get('color_id')
    size_id = request.GET.get('size_id')
    q = request.GET.get('q')
    if cat_id:
        products = products.filter(categories=cat_id)
    if brand_id:
        products = products.filter(brand=brand_id)
    if color_id:
        products = products.filter(products_quantity__color=color_id)
    if size_id:
        products = products.filter(products_quantity__size=size_id)
    if q:
        products = products.filter(title__icontains=q)

    context = {
        "categories": categories,
        "brands": brands,
        "colors": colors,
        "sizes": sizes,
        "products": products,
    }
    return render(request, 'products.html', context)
    return render(request, 'products.html')

def checkout_page_views(request):
    return render(request, 'checkout.html')

# def contact_page_views(request):
#     # if request.method == "POST":
#     #     form = ContactForm(request.POST)
#     #     if form.is_valid():
#     #         form.save(commit=False)
#     #         form.result = 1313
#     #         form.save()
#     #         return redirect('bloc:contact')
#     #     else:
#     #         errors = []
#     #         for key, value in form.errors.items():
#     #             for error in value:
#     #                 errors.append(error)
#     #         context = {
#     #             "errors": errors
#     #         }
#     #         return render(request, 'contact.html', context)
#     #
#     # else:
#         return render(request, 'contact.html')

def dashboard_page_views(request):
    return render(request, 'dashboard.html')

def faq_page_views(request):
    return render(request, 'faq.html')

# def login_page_views(request):
#     return render(request, 'login.html')

def product_det_page_views(request):
    return render(request, 'product-detail.html')

def wishlist_page_views(request):
    return render(request, 'wishlist.html')


def pages_about_views(request):
    return render(request, 'about.html')