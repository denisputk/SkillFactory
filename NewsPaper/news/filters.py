from django_filters import FilterSet, DateFilter
from django import forms

from .models import Post


class PostFilter(FilterSet):
    date_create__gt = DateFilter(field_name='post_created', label='Begining from', widget=forms.DateInput(
        attrs={'type': 'date'}), lookup_expr='date__gte')
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
        }
