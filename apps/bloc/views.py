import threading

from django.shortcuts import render

from django.db.models import Count

from django.views.generic import ListView, DetailView

from .models import BlogModel, BlogCategoryModel, BlogTagModel
from .utils import check_blog_view


class BlogListView(ListView):
    template_name = 'blog-list.html'

    def get_queryset(self):
        return BlogModel.objects.filter(
            status=BlogModel.BlogStatus.PUBLISHED
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        categories = BlogCategoryModel.objects.all()
        tags = BlogTagModel.objects.all()
        most_popular_blogs = (
            BlogModel.objects
            .annotate(views_count=Count('views', distinct=True))
            .order_by('-views_count')[:4]
        )
        context["blogs"] = self.get_queryset()
        context["categories"] = categories
        context["tags"] = tags
        context["most_popular_blogs"] = most_popular_blogs

        return context


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    queryset = BlogModel.objects.all()
    context_object_name = 'blog'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()

        # update view count of blog
        threading.Thread(target=check_blog_view, args=(self.request, blog,)).start()

        categories = BlogCategoryModel.objects.all()
        tags = BlogTagModel.objects.all()
        related_blogs = BlogModel.objects.filter(
            category__in=blog.category.all()
        ).exclude(id=blog.id).distinct()
        most_popular_blogs = (
            BlogModel.objects
            .annotate(views_count=Count('views', distinct=True))
            .order_by('-views_count')[:4]
        )

        context["blogs"] = self.get_queryset()
        context["categories"] = categories
        context["tags"] = tags
        context["most_popular_blogs"] = most_popular_blogs
        context["related_blogs"] = related_blogs

        return context

def home_page_views(request):
    return render(request, 'home.html')

def page_views_404(request):
    return render(request, '404.html')

def blog_detail_views(request):
    return render(request, 'blog-detail.html')

def cart_page_views(request):
    return render(request, 'cart.html')

def checkout_page_views(request):
    return render(request, 'checkout.html')

def dashboard_page_views(request):
    return render(request, 'dashboard.html')

def faq_page_views(request):
    return render(request, 'faq.html')

def wishlist_page_views(request):
    return render(request, 'wishlist.html')


def pages_about_views(request):
    return render(request, 'about.html')