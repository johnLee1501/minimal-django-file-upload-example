from django.urls import path
from .views import my_view, run_view

urlpatterns = [
    path('', my_view, name='my-view'),
    path('run/', run_view, name='run_view'),
]
