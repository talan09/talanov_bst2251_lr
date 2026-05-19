from django.shortcuts import render
from django.http import Http404
from lab3.articles.models import Article
from django.shortcuts import redirect

# Create your views here.
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            
            if form["text"] and form["title"]:
                # Проверка на уникальность названия
                if Article.objects.filter(title=form["title"]).exists():
                    # Если статья с таким названием уже существует
                    form['errors'] = "Статья с таким названием уже существует. Пожалуйста, придумайте другое название."
                    return render(request, 'create_post.html', {'form': form})
                else:
                    # если поля заполнены без ошибок и название уникально
                    article = Article.objects.create(
                        text=form["text"],
                        title=form["title"],
                        author=request.user
                    )
                    return redirect('article', article_id=article.id)
                # перейти на страницу поста
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404
