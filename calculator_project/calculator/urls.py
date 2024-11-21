from django.urls import path
from .views import *

app_name = "calculator"
urlpatterns = [
    path("", calculator_view, name="calculator"),
]
