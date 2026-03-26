from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse


def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Invalid login')

    return render(request, 'login.html', {'form': form})
