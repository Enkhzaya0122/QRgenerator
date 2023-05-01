from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests
import json
import base64

@api_view(["POST","GET"])
def headerBase(request):
    return render(template_name = 'index.html',request = request)

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
        
            jsonFile = json.loads(r.text)
            context =   {
                            'mymembers': jsonFile['data'],
                        }
    elif request.method == "POST":
        print("Hello")
        if request.POST.get('download'):
            base64_string = str(request.POST.get('base64_code'))
            print(base64_string)
            image_bytes = base64.b64decode(base64_string)
            filename = "image.png"
            response = HttpResponse(content_type='image/png')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            response.write(image_bytes)
            context =   {
                            'mymembers': response,
                        }
    return render(template_name = 'index.html',request = request,context=context)


def login(request):
    return render(template_name = 'login.html',request = request)

def forgot1(request):
    return render(template_name = 'forgot/forgot1.html',request = request)

def forgot2(request):
    return render(template_name = 'forgot/forgot2.html',request = request)

def forgot3(request):
    return render(template_name = 'forgot/forgot3.html',request = request)

def register(request):
    return render(template_name = 'register.html',request = request)