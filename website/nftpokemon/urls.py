from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('battle/<str:address>/<int:token_id>', views.battle, name='battle'),
]