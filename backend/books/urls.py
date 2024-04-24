from django.urls import path

from . import views

urlpatterns=[
    path('<int:pk>/', views.book_detail_view)
]