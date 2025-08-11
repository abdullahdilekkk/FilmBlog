from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .import models
import requests

@login_required
def add_to_favorites(request, movieId):
    apiKey = "6cb44f80117b072e805442442ffaaa47"
    url = f"https://api.themoviedb.org/3/movie/{movieId}?api_key={apiKey}&language=tr-TR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json() 
        


        farkliKayit =  models.FavotiteMovies.objects.filter(user=request.user, movieId=movieId).exists()
        #var ise exits() true döndrür

        if  not farkliKayit:#eğer farklı ise burada favoriteMovies objesi oluşturuyoruz
            models.FavotiteMovies.objects.create(
                user = request.user,
                movieId = movieId,
                title = data.get("title"),
                poster_path = data.get("poster_path"),
                release_date = data.get("release_date"),
                vote_average = data.get("vote_average")
                
            )
    return redirect('takmaAdHomePage')


@login_required
def favorites_list(request):
    # 1) Sadece giriş yapan kullanıcının favori filmleri alınır
    favMovies = models.FavotiteMovies.objects.filter(user=request.user)

    return render(request, 'favorites/favoritesPage.html',{'favMovies':favMovies})


@login_required
def deleteMovie(request, movieId):
    # 1. Bu kullanıcıya ait o movieId'li kayıt var mı kontrol et
    movie = models.FavotiteMovies.objects.filter(user=request.user, movieId=movieId).first()

    # 2. Varsa sil
    if movie:
        movie.delete()

    # 3. Favoriler sayfasına geri döndür
    return redirect('favorites_list')