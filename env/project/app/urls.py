

from django.urls import path
from. import views

urlpatterns = [
    path("",views.index,name='index'),
    path("register",views.register,name='register'),
    path("signup",views.signup,name='signup'),
    path("loginn",views.loginn,name='loginn'),
    path("admission",views.admission,name='admission'),
    path("details",views.details,name='details'),
    path("connect",views.connect,name='connect'),
]
