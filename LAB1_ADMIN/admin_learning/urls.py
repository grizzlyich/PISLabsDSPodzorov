from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет, Мир! (LAB1_ADMIN)")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
