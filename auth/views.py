from django.http import HttpResponse
from django.template import loader

def login(request):
    template = loader.get_template('page/auth/login.html')
    return HttpResponse(template.render())