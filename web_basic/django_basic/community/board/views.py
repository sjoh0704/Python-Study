from django.db import models
from django.shortcuts import render
from .models import Board
# Create your views here.


def board_list(request):
    board = Board.objects.all().order_by("-id")

    return render(request, 'board_list.html', {"boards": board})
