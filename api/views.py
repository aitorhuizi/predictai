from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
from .serializers import TuSerializer

import json
import pickle as pkl

# Create your views here.
class PredictAI_APIView(APIView):

    def post(self, request):

        serializer = TuSerializer(data=request.data)

        if serializer.is_valid():
            # Aquí manejas los datos validados
            validated_data = serializer.validated_data

            base_path = str(settings.BASE_DIR).replace('\\', '/')

            target_col = request.data.get('target_col')

            with open(base_path + f'/api/data/clasificador_{target_col}.pickle', 'rb') as file:
                model = pkl.load(file)

            X = json.loads(request.data.get('X'))
            yPred = model.predict(X)

            return Response({'yPred':yPred}, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusView(APIView):
 
    def get(self, request, *args, **kwargs):

        return Response({"status": "OK"}, status=status.HTTP_200_OK)