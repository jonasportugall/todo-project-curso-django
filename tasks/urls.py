from django.urls import path

from . import views

urlpatterns = [
    path('hellowold/', views.hellowold),
]
