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
from rest_framework.decorators import api_view
from . import serializers
from departments.models import Subject



# Create your views here.
class ResultViews(viewsets.ModelViewSet):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self,request):
        result = models.Result.objects.all()
        serializer = serializers.ResultSerializer(result,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        result = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ResultSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def create(self , request):
        serializer = serializers.ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,requset, pk=None):
        result = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ResultSerializer(result, data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def parial_padate(self, request, pk=None):
        result = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ResultSerializer(result,data=request.data, parial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request, pk=None):
        result = get_object_or_404(self.queryset,pk=pk)
        result.delete()
        return Response({"message": "course result deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def result_bulk_upload_view(request):
    if request.method == "POST":
        file = request.FILES.get("result-file")
        
        bulk_upload = models.CourseResultUpload.objects.create(
            csv_file=file
        )
        
        if bulk_upload:
            return Response({"message":"file uploaded"})
        else:
            return Response({"message":"file not uploaded "})
