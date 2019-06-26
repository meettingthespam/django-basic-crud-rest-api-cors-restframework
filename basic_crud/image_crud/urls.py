from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListImages.as_view()),
    path('<int:pk>/', views.DetailImage.as_view()),
]
