from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_flat, name='render_flat'),
]
