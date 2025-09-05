from django.shortcuts import render


from apps.shop.models import ProductCategory, ProductSize, ProductColor, ProductModel, ProductBrand
def product_page_views(request):
    categories = ProductCategory.objects.all()
    brands = ProductBrand.objects.all()
    colors = ProductColor.objects.all()
    sizes = ProductSize.objects.all()
    products = ProductModel.objects.all()
    context = {
        "categories": categories,
        "brands": brands,
        "colors": colors,
        "sizes": sizes,
        "products": products,
    }
    return render(request, 'products.html', context)
