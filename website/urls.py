from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('index', views.index, name='index'),
    path('assignment1', views.assignment1),
    path('', views.homepage, name='home'),
]
