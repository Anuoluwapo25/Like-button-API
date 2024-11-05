from django.urls import path
from .views import ArticleDetailView, ArticleLikeView

urlpatterns = [
    path('articles/<int:article_id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:article_id>/like/', ArticleLikeView.as_view(), name='article-like'), 
]
