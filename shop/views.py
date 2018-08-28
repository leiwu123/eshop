from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product

def index(request):
	text_var = 'This is my first django app web page.'
	return HttpResponse(text_var)


def allProdCat(request, c_slug=None):
	c_page = None
	products = None
	if c_slug!=None:
		c_page = get_object_or_404(Category, slug=c_slug)
		# print(c_slug)
		# print(c_page)
		products = Product.objects.filter(category=c_page, available=True)
		print(products)
	else: 
		products = Product.objects.all().filter(available=True)
		# print(products)
	return render(request, 'shop/category.html', {'category':c_page, 'products':products})