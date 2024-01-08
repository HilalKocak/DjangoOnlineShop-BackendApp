from .views import OrderView
from django.urls import path

urlpatterns = [
    
    path('order/', OrderView.as_view(), name = 'order'),

]