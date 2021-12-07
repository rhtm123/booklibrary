from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

from book.models import Book, Publisher, BookAuthor


def demo_view(request):
    d = {"key1": [2, 4, 7, 8], "key2": "Some random value", "key3": True}
    return render(request, "demo.html", d)


def home_view(request):
    book_objects = Book.objects.all()
    d = {"books": book_objects}
    return render(request, "home.html", d)


def contact_view(req):
    return HttpResponse("Contact View")


def about_view(req):
    return HttpResponse("About Page")
