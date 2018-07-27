from django.shortcuts import render
from mysite.models import Product
from django.template.loader import get_template
import random
from django.http import HttpResponse,Http404
from mysite import models


def index(request):
    products = models.Product1.objects.all()
    return render(request, 'mysite/index.html',{'products':products})



def about(request):
    template = get_template('mysite/about.html')
    quotes = ['今日事，今日毕',
              '种瓜的瓜，种豆得豆',
              '一个人的个性就是他的命运',
              '知识就是力量'
    ]
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)


def listing(request,list_date):
    return render(request,'mysite/list.html', {'ld': list_date})
    #html="<h2>post date is {}</h2><hr>".format(list_date)
    #return HttpResponse(html)
