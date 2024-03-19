from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name="boot"),
    path('qwerty/', views.create, name="create_form"),
    path('add/', views.indeе),
    path('reg/', views.register, name='reg'),
    path('cookie/', views.setcookie),
    path('cooki/', views.set_cookie),
    path('dell/', views.deletercooike)
]