from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def get_user(request):
    user = request.user
    return render(request, 'profil/account_page.html', {"user":user})