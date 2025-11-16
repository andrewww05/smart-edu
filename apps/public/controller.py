from django.shortcuts import render

class PublicController:
    def home(self, request):
        return render(request, 'page/public/home.html')
