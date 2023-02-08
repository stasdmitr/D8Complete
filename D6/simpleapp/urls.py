from django.urls import path
# Импортируем созданные нами представления
from .views import *

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   path('', NewsList.as_view(), ),
   path('', ArticlesList.as_view(), ),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения

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