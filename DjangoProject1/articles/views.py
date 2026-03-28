from django.http import Http404, HttpResponseNotAllowed, HttpResponseForbidden
from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render

from articles.models import Article


def archive(request):
    return render(request, 'archive.html', {"posts":
                                                Article.objects.all()})
def index(request):
    return render(request, 'l9.html', {"posts":
                                                Article.objects.all()})

def show(request, article_id):
    post = Article.objects.get(id=article_id)
    return render(request, 'article.html', {"post": post})


def create_post(request):

    if not request.user.is_authenticated:
        raise Http404("Только авторизованные пользователи могут создавать статьи")

    if request.method == "POST":

        form = {
            'title': request.POST.get('title', ''),
            'text': request.POST.get('text', '')
        }


        if form["text"] and form["title"]:

            article = Article.objects.create(
                title=form["title"],
                text=form["text"],
                author=request.user
            )

            return redirect('articles:archive')
        else:

            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:

        return render(request, 'create_post.html')
