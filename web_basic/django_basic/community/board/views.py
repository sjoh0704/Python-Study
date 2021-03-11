from django.db import models
from django.shortcuts import redirect, render
from .models import Board
from .form import BoardForm

from fcuser.models import Fcuser
# Create your views here.


def board_write(request):

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            contents = form.cleaned_data['contents']

            board = Board()
            board.title = title
            board.contents = contents
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            board.writer = fcuser

            board.save()

            return redirect("/board/list")
    else:

        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    board = Board.objects.all().order_by("-id")

    return render(request, 'board_list.html', {"boards": board})
