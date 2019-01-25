from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
from article.models import Article


def list_article(request):
    articles = Article.objects.all()
    data = {
        'articles': articles,
    }
    return render(request, 'list.html', data)


def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    data = {
        'article': article,
    }
    return render(request, 'detail.html', data)


def create_article(request):
    if request.method == 'POST':
        # 값 받아오는 법 2가지->.get 이 더 나음
        title = request.POST.get('title', None)
        content = request.POST['content']
        article = Article.objects.create(
            title = title,
            content = content
        )
        # redirect->다른 url로 가게 하는 것
        return redirect(reverse('list')) #/->루트 url로 가는 것(우리가 기존에 루트 디렉토리 설정함)
    return render(request, 'create.html')