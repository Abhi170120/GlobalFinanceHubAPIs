# myapp/views.py
import requests
from rest_framework.views import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

@api_view(['GET'])
def stock_data_view():
    api_key = settings.TWELVE_DATA_API_KEY
    url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    except requests.exceptions.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
