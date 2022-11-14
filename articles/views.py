from django.shortcuts import render, redirect
from .models import Article
from django.http import Http404

def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})

def create_post(request):
	if request.method == "GET":
		return render(request, 'create_post.html', {})
	else:
		form = {
			'text': request.POST['text'], 'title': request.POST['title']
		}
		if form['text'] and form['title']:
			if Article.objects.filter(text=form['text'], title=form['title']):
				form['erorrs'] = u"Такая статья уже существует"
			Article.objects.create(text=form['text'], title=form['title'])
			return redirect('archive')
		else:
			form['errors'] = u"Не все поля заполнены"
			return render(request, 'create_post.html', {'from': form})




def get_article(request, article_id):
	try:
		post = Article.objects.get(id=article_id)
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		raise Http404

