from django.urls import path
from . import views

urlpatterns = [
    path('tuber_contact', views.tuber_contact, name="tuber_contact"),
]
