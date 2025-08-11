from django.shortcuts import render
from . import models
import requests



def homePage(request):

    apiKey = "6cb44f80117b072e805442442ffaaa47"

    url = f"https://api.themoviedb.org/3/movie/popular?api_key={apiKey}&language=tr-TR&page=1"

    try:
        response = requests.get(url)
        data = response.json()
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"API isteği başarısız oldu: {e}")
    

    type_map = {
            28: "Aksiyon",
            12: "Macera",
            16: "Animasyon",
            35: "Komedi",
            80: "Suç",
            18: "Dram",
            10751: "Aile",
            27: "Korku",
            10749: "Romantik",
            878: "Bilim Kurgu",
            53: "Gerilim",
            14: "Fantastik",
            36: "Tarih",
            99: "Belgesel",
        }

    for m in data["results"]:
        type_ids = m.get("genre_ids", [])
        m["type"] = [type_map.get(A, "Bilinmiyor") for A in type_ids]

    return render(request, 'film/homePage.html', {'movies':data["results"]})





   