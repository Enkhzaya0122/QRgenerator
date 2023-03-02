from django.contrib import admin
from django.urls import path,include
from qrFrontEnd import urls as frontendUrls
from qrBackEnd import urls as backendUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(frontendUrls)),
    path('backend/',include(backendUrls)),
]
