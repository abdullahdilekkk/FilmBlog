from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Django kullanıcıyı tanır
            return redirect('takmaAdHomePage')  # Örnek: anasayfaya yönlendir
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı.')

    return render(request, 'registration/login.html')


from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('takmaAdHomePage')  # Login sayfasına gönder
