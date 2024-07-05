from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getData),
    path('api/hello/', views.hello, name="hello"),
]
