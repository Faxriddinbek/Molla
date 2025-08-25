from django.shortcuts import render

def about_page_views(request):
    return render(request, 'blog-list.html')


def home_page_views(request):
    return render(request, 'home.html')
