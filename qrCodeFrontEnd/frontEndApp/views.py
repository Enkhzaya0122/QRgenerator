from django.shortcuts import render

def index(request):
    return render(template_name = 'index.html',request = request)

def forgot1(request):
    return render(template_name = 'forgot/forgot1.html',request = request)

def forgot2(request):
    return render(template_name = 'forgot/forgot2.html',request = request)

def forgot3(request):
    return render(template_name = 'forgot/forgot3.html',request = request)
