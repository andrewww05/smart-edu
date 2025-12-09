from django.shortcuts import render

class PublicController:
    def home(self, request):
        return render(request, 'page/public/home.html')

    def faq(self, request):
        return render(request, 'page/public/faq.html')

    def map(self, request):
        return render(request, 'page/public/map.html')
