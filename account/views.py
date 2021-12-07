from django.http.response import HttpResponse
from django.shortcuts import redirect, render, redirect

# Create your views here.
from django.contrib.auth.models import User


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def protect_view1(request):
    if request.user.is_authenticated:
        return HttpResponse("Everything is good. You can access this page")
    else:
        return HttpResponse("Login is required to access this page. ")


@login_required(login_url="/account/login/")
def protect_view2(request):
    return HttpResponse("You can access this page.")


def logout_view(request):
    logout(request)
    return HttpResponse("You are successfully logged out")


def login_view(request):
    next_page = request.GET.get("next")
    d = {"is_login": False}
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]

        user = authenticate(username=u, password=p)

        if user is not None:
            login(request, user)
            d["is_login"] = True
            if next_page:
                return redirect(next_page)
            return render(request, "account/login.html", d)
        else:
            return render(request, "account/login.html", d)

    return render(request, "account/login.html", d)


def register_view(request):
    d = {"is_signup": False, "error": False}
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]
        fn = request.POST["fn"]
        ln = request.POST["ln"]
        try:
            u = User.objects.create_user(
                username=u, password=p, first_name=fn, last_name=ln
            )
            u.save()
            d["is_signup"] = True
            return render(request, "account/signup.html", d)
        except:
            d["error"] = True
            return render(request, "account/signup.html", d)
        # print("This method is called")
    return render(request, "account/signup.html", d)
