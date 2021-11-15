from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('battle', views.battle, name='battle'),
    path('battle/<str:address>/<int:token_id>', views.battleknown, name='battle'),
]