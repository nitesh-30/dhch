from django.urls import path
from .views import index,signup,login
urlpatterns = [
    
                path('',index,name="homepage"),
                path('signup',signup,name="signup"),
                path('login',login,name="login"),

              ]