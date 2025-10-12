from django.http import HttpResponse
from django.template import loader

def register(request):
    template = loader.get_template('page/auth/register.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('page/auth/login.html')
    return HttpResponse(template.render())