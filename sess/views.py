from django.shortcuts import render
from django.template import RequestContext
from sess.fms import LoginForm
from django.template.loader import get_template
from django.http import HttpResponse


def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['user_name']
            usercolor = request.POST['user_color']
            message = "登录成功"
        else:
            message = "请检查输入的内容"
    else:
        login_form = LoginForm()

    # template = get_template('sess/login.html')
    #request_context = RequestContext(request)
    # request_context.push(locals())
    # html = template.render(request_context)
    # response = HttpResponse(html)
    return render(request,'sess/login.html',locals())
    try:
        if username: response.set_cookie('username', username)
        if username: response.set_cookie('usercolor', usercolor)
    except:
        pass
    return render(request, 'sess/login.html', locals())