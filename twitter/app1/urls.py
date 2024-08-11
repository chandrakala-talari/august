from django.urls import path
from app1 import views
urlpatterns=[
    path('',views.homeview,name="homepage"),
    path('login',views.loginview,name="loginpage"),
    path('register',views.registerview,name="registerpage"),
    path('profile',views.profileview,name="profilepage"),
    path('create',views.createview,name="createpage"),
    path('delete/<int:rid>',views.deleteview,name="deletepage"),
    path('single/<int:rid',views.singleview,name="singlepage"),
    path('logout',views.logoutview,name="logoutpage"),
]