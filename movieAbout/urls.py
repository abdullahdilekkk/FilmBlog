from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.movieAbout, name="takmaAdAbout"),
]
