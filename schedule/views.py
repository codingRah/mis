from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializers



# Create your views here.
class ScheduleViews(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self,request):
        schedule = models.Schedule.objects.all()
        serializer = serializers.ScheduleSerializer(schedule,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        schedule = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ScheduleSerializer(schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self , request):
        serializer = serializers.ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,requset, pk=None):
        schedule = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ScheduleSerializer(schedule, data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def parial_padate(self, request, pk=None):
        schedule = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ScheduleSerializer(schedule,data=request.data, parial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request, pk=None):
        schedule = get_object_or_404(self.queryset,pk=pk)
        schedule.delete()
        return Response({"message": "schedule deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    