from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import EventCreateSerializer


class EventAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = EventCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.create(request.data)
            return Response({'created': request.data}, status=HTTP_201_CREATED)
        return Response({'message': 'Invalid data'}, status=HTTP_400_BAD_REQUEST)
