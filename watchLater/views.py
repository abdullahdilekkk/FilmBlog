from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
import requests
from .models import WatchLater

@login_required   #Kullanıcı, bu fonksiyonu çağırmadan önce giriş yapmış mı kontrol eder.
def watch_later_list(request):
    user_movies = WatchLater.objects.filter(user=request.user)
    movie_list = []
    apiKey = "6cb44f80117b072e805442442ffaaa47"
    for item in user_movies:
        movie_id = item.movie_id
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={apiKey}&language=tr-TR')
        if response.status_code == 200:
            movie_data = response.json()
            movie_list.append(movie_data)

    return render(request, 'users/watchLater.html', {'movies': movie_list})

@login_required
def add_to_watch_later(request, movie_id):
    # Aynı film varsa tekrar ekleme
    if not WatchLater.objects.filter(user=request.user, movie_id=movie_id).exists():
        WatchLater.objects.create(user=request.user, movie_id=movie_id)
    return redirect('takmaAdHomePage')  # Anasayfaya dön

@login_required
def delete_to_watchList(request, movie_id):
    
    film = get_object_or_404(WatchLater, user=request.user, movie_id=movie_id)
    film.delete()
    return redirect('watchLater')  # veya hangi sayfaya dönmek istiyorsan