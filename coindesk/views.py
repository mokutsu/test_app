from rest_framework import generics
from rest_framework.response import Response
from coindesk.helpers import get_coindesk_data
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


# import services

class CoinDeskListCreate(APIView):
    def get(self, request):
        requested_data = get_coindesk_data()
        if not requested_data:
            return Response(requested_data, status=400)
        return Response(requested_data, status=200)
