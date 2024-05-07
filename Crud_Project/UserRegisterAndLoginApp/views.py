from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


# user register function
def register(request):
    if request.method == "GET":
        fm = RegisterForm()
    elif request.method == "POST":
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "ACCOUNT CREATED SUCCESSFULLY!")
            fm = RegisterForm()
    return render(request, "register.html", {"form": fm})


def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            upass = fm.cleaned_data["password"]
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, "Login SuccessFully!!")
                return render(request, "Profile.html")
                # return HttpResponseRedirect("/Profile/")
    else:
        fm = AuthenticationForm()
    return render(request, "user_login.html", {"form": fm})
    # return render(request, "user_login.html")


def Profile(request):
    if request.user.is_authenticated:
        return render(request, "Profile.html", {"name": request.user})
    else:
        return HttpResponseRedirect("/user_login/")
    # return render(request, "Profile.html")


# user logout function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/user_login/")
