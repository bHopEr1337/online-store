from django.urls import path
from frontMain.views import *

app_name = 'frontMain'

urlpatterns = [
    path('', index, name='index'),
    path('house/', house, name='house'),
    path('price/', price, name='price'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('contact/test/', test, name='test'),
]