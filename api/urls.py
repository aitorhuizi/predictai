from django.urls import path
from .views import PredictAI_APIView, StatusView

urlpatterns = [
    path('predict', PredictAI_APIView.as_view()),
    path('status', StatusView.as_view())
]