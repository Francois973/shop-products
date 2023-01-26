from django.shortcuts import render
from shop.models import Product

# Create your views here.
def index(request):

    product = Product.objects.all()
    return render(request, "shop/index.html", context={"products": product})
