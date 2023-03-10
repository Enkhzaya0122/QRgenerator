from django.urls import path
from .services import qrcode
from .services import users

urlpatterns = [
    path('users/', users.mainFunction),
    path('qrcode/', qrcode.mainFunction),
]
