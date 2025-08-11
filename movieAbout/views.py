from django.shortcuts import render
import requests

# Create your views here.
def movieAbout(request, id):
    apiKey = "6cb44f80117b072e805442442ffaaa47"
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key={apiKey}&language=tr-TR&page=1"

    try:
        response = requests.get(url)
        data =response.json()
        

    except requests.exceptions.RequestException as e:
        raise Exception(f"API isteği başarısız oldu: {e}")
    
    return render(request, 'movieAbout/movieAbout.html', {"movie":data})