from django.shortcuts import render, redirect
from .models import Article
import time
# Create your views here.


def index(request):
    articles = Article.objects.all()
    movie_numbers = Article.objects.filter(type__contains="영화").count()
    drama_numbers = Article.objects.filter(type__contains="드라마").count()
    programing_numbers = Article.objects.filter(
        type__contains="프로그래밍").count()
    return render(request, 'index.html', {'movie_numbers': movie_numbers, 'drama_numbers': drama_numbers, 'programing_numbers': programing_numbers})


def new(request):
    if request.method == "POST":
        print(request.POST)
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            wrote_time=time.strftime('%c', time.localtime(time.time())),
            type=request.POST['type']
        )
        return redirect('detail', article_pk=new_article.pk)

    return render(request, 'new.html')


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article': article})


def movie_list(request):
    articles = Article.objects.filter(type__contains="영화")
    return render(request, 'movie.html', {'articles': articles})


def drama_list(request):
    articles = Article.objects.filter(type__contains="드라마")
    return render(request, 'drama.html', {'articles': articles})


def programing_list(request):
    articles = Article.objects.filter(type__contains="프로그래밍")
    return render(request, 'programing.html', {'articles': articles})
