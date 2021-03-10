from django.db import models
from django.shortcuts import redirect, render
from .models import Board
from .form import BoardForm
# Create your views here.


def board_write(request):

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():

            # request.session['user'] = form.user_id
            title = request.POST.get("title", None)
            contents = request.POST.get("contents", None)

            board = Board(contents=contents, title=title,
                          writer=None, registered_dttm=None)
            board.save()

            return redirect("/board/list")
    else:

        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    board = Board.objects.all().order_by("-id")

    return render(request, 'board_list.html', {"boards": board})
