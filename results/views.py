from django.shortcuts import render
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
from departments.models import Subject



# Create your views here.


class ResultViews(viewsets.ModelViewSet):

    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    # permission_classes= [IsAuthenticated,]
    
    def list(self, request):
        serializer = serializers.ResultSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        course_status = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ResultSerializer(course_status)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        course_status = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ResultSerializer(course_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course_status = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ResultSerializer(course_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        course_status = get_object_or_404(self.queryset, pk=pk)
        course_status.delete()
        return Response({"message": "status deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


