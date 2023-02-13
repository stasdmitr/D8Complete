from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class News(models.Model):
    date = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    name = models.CharField(max_length=50, unique=True, verbose_name='Заголовок')
    description = models.TextField(default="Ваша новость", verbose_name='Содержание')

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


class Articles(models.Model):
    date = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    name = models.CharField(max_length=50, unique=True, verbose_name='Заголовок')
    description = models.TextField(default="Ваша статья", verbose_name='Содержание')

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
