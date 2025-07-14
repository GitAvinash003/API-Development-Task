from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import FormData
from .serializers import FormDataSerializer

# POST /api/form_data/
class FormDataCreateAPIView(generics.CreateAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer

# GET /api/form_data/<id>/
class FormDataRetrieveAPIView(generics.RetrieveAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer
