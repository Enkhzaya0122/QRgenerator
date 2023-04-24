from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
import json

@api_view(["POST","GET"])
def index(request):
    if request.method == 'GET': 
        if request.GET.get('submit'):
            requestJSON = {
    "action": "",
} 
            requestJSON["action"] = "getUsers"   
            print(json.dumps(requestJSON)) 
            r = requests.get("http://127.0.0.1:8080/users/",
                data=json.dumps(requestJSON),
                headers={'Content-Type': 'application/json' }
            )
            print(r)
            a = r.text
            print(a)

    return render(template_name = 'index.html',request = request)

def forgot1(request):
    return render(template_name = 'forgot/forgot1.html',request = request)

def forgot2(request):
    return render(template_name = 'forgot/forgot2.html',request = request)

def forgot3(request):
    return render(template_name = 'forgot/forgot3.html',request = request)

def register(request):
    return render(template_name = 'register.html',request = request)