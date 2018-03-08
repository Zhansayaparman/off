from django.urls import path
from . import views
# local url
urlpatterns = [
    path('', views.index, name='index'),
]