from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password


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