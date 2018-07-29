from django.shortcuts import render
from mysite.models import Product
from django.template.loader import get_template
from django.template import RequestContext
import random
from django.http import HttpResponse,Http404
from mysite import models
from mysite import fms

def contact(request):
    form = fms.ContactForm()
    request_context = RequestContext(request)
    return render(request,'myform/contact.html',locals())


def indexform(request):
    posts = models.Post.objects.filter(enable=True).order_by("-pub_time")[0:30]
    moods = models.Mood.objects.all()

    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['user_mood']
    except:
        user_id = None
        message = "如要发布信息，每个位置都要填写"
    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood,nickname=user_id,def_pass=user_pass,message=user_post)
        post.save()
        message="成功存储[{}]".format(user_pass)
    return render(request,'myform/index.html',locals())


def myform(request):
    return render(request,"myform/index.html")


def index(request):
    products = models.Product1.objects.all()
    return render(request, 'mysite/index.html',{'products':products})


def detail(request, id):
    try:
        product = models.Product1.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    return render(request,'mysite/detail.html',{'images':images,'puoduct':product})


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
