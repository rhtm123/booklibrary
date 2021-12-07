from django.db import models

from django.contrib.auth.models import User


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    detail = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.

LANGUAGE_CHOICES = (("en", "English"), ("hi", "Hindi"))


class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    detail = models.TextField()
    img = models.ImageField(upload_to="book", null=True, blank=True)
    mrp = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=255, default="en")
    pub_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    # authors = models.ManyToManyField()

    ## tracking
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} {self.author.username}"
