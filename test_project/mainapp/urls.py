from django.urls import path, include

from mainapp import views

urlpatterns = [
    path('', views.HelloAPIView.as_view()),
]

