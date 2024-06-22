from django.urls import path
from .views import stock_data_view
urlpatterns = [
    path('data/', stock_data_view, name='data'),
]
