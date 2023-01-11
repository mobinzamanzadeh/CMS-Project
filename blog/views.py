from typing import Any

from django.shortcuts import render, HttpResponse
from blog.models import Blog


def home(request):
    return render(request, 'index.html')


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    return render(request, 'bloghome.html', context)


def blogpost(request, slug):      # This is SLUG
    blog = Blog.objects.filter(slug=slug).first()
    context = {"blog": blog}
    return render(request, 'blogpost.html', context)


def search(request):
    return render(request, 'search.html')


def contact(request):
    return render(request, 'contact.html')
