from django.shortcuts import render
from events.models import Category

# Create your views here.
def category_list_create(request):
    categories = Category.objects.all()