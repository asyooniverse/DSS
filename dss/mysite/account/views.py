from django.shortcuts import render, redirect
from account.models import User
from django.contrib import auth
from account.forms import SignupForm

# 회원 가입
def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm']:
            user = User( user_id=request.POST['username'], user_pw=request.POST['password'])
            user.save()
            # auth.login(request, user)
            return redirect('home')

    return render(request, "signup.html")


# 로그인
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
    else:
        return render(request, "login.html")


# 로그 아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request,'home.html')


def home(request):
    return render(request, 'home.html')