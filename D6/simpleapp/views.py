from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import NewsFilter, ArticlesFilters
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response


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
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'concrete_News.html'
    context_object_name = 'news'


# Добавляем новое представление для создания товаров.
class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ("simpleapp.add_news")
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.get_or_create(user=user)[0]
            post.save()
            return self.form_valid(form)
        return redirect('news:news')


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('simpleapp.change_news')


class NewsDelete(PermissionRequiredMixin, DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('simpleapp.delete_news')


class NewsSearch(ListView):
    model = News
    template_name = 'news_search.html'
    ordering = 'name'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# ______________________________________________________________________________________


class ArticlesList(ListView):
    model = Articles
    ordering = 'name'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticlesFilters(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesDetail(DetailView):
    model = Articles
    template_name = 'concrete_Articles.html'
    context_object_name = 'articles'


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ("simpleapp.add_articles")
    form_class = ArticlesForm
    model = Articles
    template_name = 'articles_edit.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.get_or_create(user=user)[0]
            post.save()
            return self.form_valid(form)
        return redirect('articles:articles')


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    form_class = ArticlesForm
    model = Articles
    template_name = 'articles_edit.html'
    success_url = reverse_lazy('articles_list')
    permission_denied_message = "Доступ закрыт"
    permission_required = ('simpleapp.change_articles')


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    model = Articles
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')
    permission_required = 'simpleapp.delete_articles'


class Index(ListView):
    template_name = 'index.html'
    model = News
