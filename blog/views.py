from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "titles.html", {'blogs': blogs})


def blog_article(request,article_id):
    #article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, 'content.html', {'article': article, 'publish': pub})


def hello(request):
    return render(request, 'hello.html')


def dtime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)


