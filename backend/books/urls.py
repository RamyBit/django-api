from django.urls import path

from . import views

urlpatterns=[
    path('', views.book_create_view),
    path('<int:pk>/', views.book_detail_view),
]