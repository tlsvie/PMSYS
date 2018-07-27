from django.shortcuts import render
from account.forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse("欢迎，")
            else:
                return HttpResponse("对不起")
        else:
            return HttpResponse('invalid login')
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "login.html", {"form": login_form})