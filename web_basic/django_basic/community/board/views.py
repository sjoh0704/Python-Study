from django.db import models
from django.shortcuts import redirect, render
from .models import Board
from .form import BoardForm

from fcuser.models import Fcuser
# Create your views here.


def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'board_detail.html', {"board": board})


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
            # primary key가 userid인 row을 가져온다.
            fcuser = Fcuser.objects.get(pk=user_id)
            # fcuser = Fcuser.objects.all() 모든 오브젝트를 가져오는 것일듯?
            board.writer = fcuser

            board.save()

            return redirect("/board/list")
    else:

        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    board = Board.objects.all().order_by("-id")

    return render(request, 'board_list.html', {"boards": board})
