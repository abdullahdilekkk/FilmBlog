from django.shortcuts import render, get_object_or_404
from .models import Category, Movie

def category_list(request):
    categories = Category.objects.all().order_by("name")  # tüm kategorileri listele
    return render(request, "categories/category_list.html", {"categories": categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, category_id=category_id)  # tek kategori
    # 🔹 ManyToMany alanı doğru şekilde kullanıldı
    movies = Movie.objects.filter(categories=category).order_by("-vote_average", "title")
    return render(request, "categories/category_detail.html", {
        "categori": category,
        "movies": movies
    })
