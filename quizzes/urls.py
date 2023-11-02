from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),

    path('new/', views.new, name='new'),
    path('check/', views.check, name='check'),
]