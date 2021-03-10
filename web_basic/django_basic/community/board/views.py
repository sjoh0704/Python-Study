from web_basic.django_basic.community.board.form import BoardForm
from django.db import models
from django.shortcuts import render
from .models import Board
from .form import BoardForm
# Create your views here.


def board_write(request):
    form = BoardForm()
    return render(request, 'board_write.html', {"form": form})


def board_list(request):
    board = Board.objects.all().order_by("-id")

    return render(request, 'board_list.html', {"boards": board})
