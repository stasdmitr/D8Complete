from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News, Articles
from .filters import NewsFilter, ArticlesFilters
from .forms import NewsForm, ArticlesForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = News
    # Используем другой шаблон — product.html
    template_name = 'concrete_News.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'news'


# Добавляем новое представление для создания товаров.
class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель товаров
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'news_edit.html'


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(ListView):
    model = News
    template_name = 'news_search.html'
    # Указываем модель, объекты которой мы будем выводить
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


# ______________________________________________________________________________________


class ArticlesList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Articles
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'articles.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ArticlesFilters(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class ArticlesDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Articles
    # Используем другой шаблон — product.html
    template_name = 'concrete_Articles.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'articles'


# Добавляем новое представление для создания товаров.
class ArticlesCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ArticlesForm
    # модель товаров
    model = Articles
    # и новый шаблон, в котором используется форма.
    template_name = 'articles_edit.html'


class ArticlesUpdate(UpdateView):
    form_class = ArticlesForm
    model = Articles
    template_name = 'articles_edit.html'


class ArticlesDelete(DeleteView):
    model = Articles
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')


class Index(ListView):
    template_name = 'index.html'
    model = News
