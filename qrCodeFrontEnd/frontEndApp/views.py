from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
import json

@api_view(["POST","GET"])
def index(request):
    context = {}
    if request.method == 'GET': 
        if request.GET.get('submit'):
            
            requestJSON =   {
                                "action": "",
                                "inputdata" : "",
                                "usernum" : "",
                            } 
            requestJSON["action"] = "qrGenerate"
            requestJSON["inputdata"] = request.GET.get('my_textarea')
            requestJSON["usernum"] = "24"
            r = requests.post("http://127.0.0.1:8080/qrcode/",
                data=json.dumps(requestJSON),
                headers={'Content-Type': 'application/json' }
            )
            print("Hello")
            jsonFile = json.loads(r.text)
            context =   {
                            'mymembers': jsonFile['data'],
                        }

    return render(template_name = 'index.html',request = request,context=context)

def forgot1(request):
    return render(template_name = 'forgot/forgot1.html',request = request)

def forgot2(request):
    return render(template_name = 'forgot/forgot2.html',request = request)

def forgot3(request):
    return render(template_name = 'forgot/forgot3.html',request = request)

def register(request):
    return render(template_name = 'register.html',request = request)