from django.urls.conf import path
from .views import *

urlpatterns = [
    path('', home),
    path('testing/', testing)
]



