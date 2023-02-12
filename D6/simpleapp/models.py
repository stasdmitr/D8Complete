from datetime import datetime
from django.db import models
from django.urls import reverse


class News(models.Model):
    date = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(default="News post")

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


class Articles(models.Model):
    date = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(default="Articles_post")

    def get_absolute_url(self):
        return reverse('articles_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name.title()


class NewsCategory(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ArticlesCategory(models.Model):
    post = models.ForeignKey(Articles, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
