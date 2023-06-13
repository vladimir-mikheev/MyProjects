from django_filters import FilterSet
from django import forms
from .models import News
import django_filters


class NewsFilter(FilterSet):
    pub_date = django_filters.DateFilter(field_name='pub_date', widget=forms.DateInput(attrs={'type': 'date'}), lookup_expr='gte')  # Используем оператор gte для отображения статей, опубликованных позже указанной даты
    class Meta:
        model = News
        fields = {
            'author': ['exact'],
            'name': ['icontains'],
            'pub_date': ['exact']
        }
