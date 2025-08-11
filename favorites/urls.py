from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:movieId>',views.add_to_favorites, name="add_to_favorites"),
    path('list/',views.favorites_list, name='favorites_list'),
    path('delete/<int:movieId>', views.deleteMovie, name='deleteMovie')
]