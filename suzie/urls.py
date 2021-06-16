from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashbord,name='dashbord'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('index',views.login,name='index'),
]