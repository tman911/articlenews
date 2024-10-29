from django.urls import path
from .views import (
    articlesPage,
    singleArticle,
    editArticle,
)

urlpatterns = [
    path('',articlesPage,name="articles"),
    path('article/<str:pk>/',singleArticle,name="article"),
    path('edit/<str:pk>',editArticle,name='edit'),
]