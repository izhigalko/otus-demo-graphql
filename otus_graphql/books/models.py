from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=254)
    birthday = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=254)
    publish_year = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey(Author, models.CASCADE, related_name='books')
