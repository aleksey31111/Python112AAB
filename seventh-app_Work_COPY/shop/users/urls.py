from django.urls import path
from . import views

urlpatters = [
    path('login/',views.login, name='login')

]