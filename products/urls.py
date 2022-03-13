from django.urls import path
from .views import *

urlpatterns = [
   path('', index),
   path('category/<int:id>/', category),
   path('product/<int:id>/', product_page)
]
