from django.urls import path,include
from servicesApp import urls

urlpatterns = [
    path('', include(urls)),
]
