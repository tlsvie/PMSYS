from django.shortcuts import render ,redirect
from django.template import RequestContext
from sess.fms import LoginForm
from django.template.loader import get_template
from django.http import HttpResponse
from sess import models


def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            try:
                user = models.User.objects.get(name = login_name)
                if user.password==login_password:
                    response = redirect('/')
                    request.session['username']=user.name
                    request.session['useremail']=user.email
                    return redirect('/')
                else:
                    message = "密码错误，再检查一次"
            except:
                message = '目前无法登陆'
        else:
            login_form = LoginForm()
        template = get_template('sess/login.html')
        request_context = RequestContext(request)
        request_context.push(locals())
        html = template.render(request_context)
        response = HttpResponse(html)
        return response


def logout(request):
    response = redirect('/')
    response.delete_cookie('username')
    return response


def index(request, pid =None, del_pass=None):
    if 'username' in request.session:
        username = request.session['username']
        useremail = request.session['useremail']
    template = get_template('sess/index.html')
    html = template.render(locals())
    return HttpResponse(html)