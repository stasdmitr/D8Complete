from django_filters import FilterSet
from .models import News, Articles


class NewsFilter(FilterSet):
    class Meta:
        model = News
        fields = {
            'name': ['icontains'],
            'description': ['icontains'],
        }


class ArticlesFilters(FilterSet):
    class Meta:
        model = Articles
        fields = {
            'name': ['icontains'],
            'description': ['icontains'],
        }
