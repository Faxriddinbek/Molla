from django.shortcuts import render

def calculate_page_views(request):
    return render(request, 'kalculate.html')


def calculate(request):
    if request.method == "POST":
        pass