from django.db import reset_queries
from django.shortcuts import redirect, render
from . import models
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .form import LoginForm


def home(request):
    user_id = request.session.get("user")
    if user_id:
        fcuser = models.Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse("home")


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


# def login(request):
#     if request.method == "GET":
#         return render(request, 'login.html')
#     elif request.method == "POST":
#         un = request.POST.get("username", None)
#         pw = request.POST.get("password", None)
#         res_data = {}
#         if not(un and pw):
#             res_data["error"] = "항목입력이 필요합니다."
#         else:
#             fcuser = models.Fcuser.objects.get(username=un)
#             print(fcuser.password)
#             if check_password(pw, fcuser.password):
#                 request.session['user'] = fcuser.id
#                 return redirect('/')
#             else:
#                 res_data["error"] = "비밀번호가 다릅니다."

#         return render(request, 'login.html', res_data)

def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            request.session['user'] = form.user_id

            return redirect('/')
    else:

        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == "GET":

        return render(request, 'register.html')
    elif request.method == "POST":

        un = request.POST.get("username", None)
        email = request.POST.get("useremail", None)
        pw = request.POST.get("password", None)
        pwck = request.POST.get("password-check",  None)
        res_data = {}

        if not (un and pw and pwck and email):
            res_data["error"] = "항목입력이 필요합니다."

        elif pw != pwck:
            res_data["error"] = "비밀번호가 다릅니다."
        else:
            fcuser = models.Fcuser(
                username=un, password=make_password(pw), useremail=email)

            fcuser.save()

        return render(request, 'register.html', res_data)
