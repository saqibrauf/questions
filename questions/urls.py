
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<id>/<slug>/', views.question, name='question'),
    path('brainly-last-q/', views.brainly_last_q, name='brainly_last_q'),
    path('add-question/', views.add_question, name='add_question'),
]
