from django.urls import path
from .views import (
    NewsList, NewsDetail, NewsFilter, NewsCreate, NewsUpdate, NewsDelete, CategoryListView, subscribe, IndexView
)
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60)(NewsList.as_view()), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search/', NewsFilter.as_view(), name='news_search'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
