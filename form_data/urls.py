from django.urls import path
from .views import FormDataCreateAPIView, FormDataRetrieveAPIView

urlpatterns = [
    path('form_data/', FormDataCreateAPIView.as_view(), name='form-data-create'),
    path('form_data/<int:pk>/', FormDataRetrieveAPIView.as_view(), name='form-data-retrieve'),
]
