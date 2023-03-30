from django.shortcuts import render

def index(request):
    return render(template_name = 'index.html',request = request)
