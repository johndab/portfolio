from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv, name='cv'),
    path('new', views.form, name='cv_form'),
]