from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('loginn',views.loginn,name='loginn'),
    path('signup',views.signup,name='signup'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addinterview',views.addinterview,name='addinterview'),
    path('addjob',views.addjob,name='addjob'),
    path('showcourse',views.showcourse,name='showcourse'),
    path('showinterview',views.showinterview,name='showinterview'),
    path('showjob',views.showjob,name='showjob'),
    path('logout',views.logout,name='logout')
]
