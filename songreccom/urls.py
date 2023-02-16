from django.urls import path
from .import views

urlpatterns=[
           path('',views.home,name='home'),
           path('songreccom/quiz',views.Quiz,name='quiz')
] 