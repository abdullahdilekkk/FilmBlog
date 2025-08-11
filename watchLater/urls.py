from django.urls import path
from. import views

urlpatterns = [
    path('add/<int:movie_id>/',views.add_to_watch_later, name="add_to_watch_later"),
    path('list/', views.watch_later_list, name="watchLater"),
    path('delete/<int:movie_id>',views.delete_to_watchList, name='deleteMovieWL')

    
]
