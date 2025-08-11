from django.contrib import admin, messages
from django.urls import path
from django.http import JsonResponse
from .models import Category, Movie
import requests

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category_id")
    change_list_template = "admin/categories/category/change_list.html"     #Kendi özel HTML dosyamızı kullanmamızı sağlar

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("sync/", self.admin_site.admin_view(self.sync_categories_and_movies))
        ]
        return custom_urls + urls

    def sync_categories_and_movies(self, request):
        if request.method == "POST":
            apiKey = "6cb44f80117b072e805442442ffaaa47"
            base_url = "https://api.themoviedb.org/3"

            # 1️⃣ Kategorileri çek
            genre_url = f"{base_url}/genre/movie/list?api_key={apiKey}&language=tr-TR"
            genre_response = requests.get(genre_url)

            if genre_response.status_code != 200:
                self.message_user(request, "❌ Kategoriler alınamadı.", level=messages.ERROR)
                return JsonResponse({"error": "Kategoriler alınamadı."}, status=500)

            genres = genre_response.json().get("genres", [])
            main_list = []

            for genre in genres:
                category_id = genre["id"]
                name = genre["name"]

                # Kategori oluştur/güncelle
                category, _ = Category.objects.update_or_create(
                    category_id=category_id,
                    defaults={"name": name}
                )

                # 2️⃣ Bu kategoriye ait filmleri çek
                movie_url = f"{base_url}/discover/movie?api_key={apiKey}&with_genres={category_id}&language=tr-TR"
                movie_response = requests.get(movie_url)

                movie_list = []

                if movie_response.status_code == 200:
                    movies = movie_response.json().get("results", [])
                    for movie_data in movies:
                        tmdb_id = movie_data["id"]
                        title = movie_data["title"]
                        poster_path = movie_data.get("poster_path", "")
                        release_date = movie_data.get("release_date", "")
                        vote_average = movie_data.get("vote_average", 0)

                        # Film oluştur/güncelle
                        movie_obj, _ = Movie.objects.update_or_create(
                            tmdb_id=tmdb_id,
                            defaults={
                                "title": title,
                                "poster_path": poster_path,
                                "release_date": release_date,
                                "vote_average": vote_average
                            }
                        )

                        # ManyToMany: Kategori ekle
                        movie_obj.categories.add(category)

                        movie_list.append({
                            "tmdb_id": tmdb_id,
                            "title": title,
                            "poster_path": poster_path,
                            "release_date": release_date,
                            "vote_average": vote_average
                        })

                main_list.append({
                    "id": category_id,
                    "name": name,
                    "movies": movie_list
                })

            self.message_user(request, "✔️ Kategoriler ve filmler başarıyla senkronize edildi.")
            return JsonResponse(main_list, safe=False, json_dumps_params={"ensure_ascii": False})

        return JsonResponse({"error": "GET isteği desteklenmiyor."}, status=405)
