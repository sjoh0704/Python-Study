from django.core import paginator
from django.db import models
from django.shortcuts import redirect, render
from .models import Board
from .form import BoardForm
from django.http import Http404
from django.core.paginator import Paginator
from tag.models import Tag
from fcuser.models import Fcuser
# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404("페이지를 찾을 수 없습니다.")
    return render(request, 'board_detail.html', {"board": board})


def board_write(request):
    if not request.session.get('user'):
        return redirect("/fcuser/login/")
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
            tags = form.cleaned_data['tag'].split(',')

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tag.add(_tag)

            return redirect("/board/list")
    else:

        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):

    all_boards = Board.objects.all().order_by("-id")
    # 페이지 번호를 get형태로 받는다.
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 4)
    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {"boards": boards})
