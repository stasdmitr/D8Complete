from django.urls import path
# Импортируем созданные нами представления
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('news/', NewsList.as_view(), name="news_list"),
    path('articles/', ArticlesList.as_view(), name="article_list"),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('<int:pk>', ArticlesDetail.as_view(), name='articles_detail'),
    path('create/', ArticlesCreate.as_view(), name='articles_create'),
    path('<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
    path('<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
]
