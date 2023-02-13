from django.urls import path
from .views import *
from protect.views import IndexView

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('news/', NewsList.as_view(), name="news_list"),
    path('articles/', ArticlesList.as_view(), name="articles_list"),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('articles/<int:pk>', ArticlesDetail.as_view(), name='articles_detail'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
    path('protect/', IndexView.as_view(), name='protect'),
    path('redirect/', redirect_view),
]
