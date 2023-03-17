from django.shortcuts import render
from . import models 
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status
from . import serializers



class AssignmentViews(viewsets.ModelViewSet):
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self,request):
        assignment = models.Assignment.objects.all()
        serailizer = serializers.AssignmentSerializer(assignment, many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        assignemt = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.AssignmentSerializer(assignemt, pk=pk)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, requset):
        serializer = serializers.AssignmentSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, requset, pk=None):
        assignment = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.AssignmentSerializer(assignment,data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def partial_update(self, requset, pk=None):
        assignment = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.AssignmentSerializer(assignment,data=requset.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, requset, pk=None):
        assignment = get_object_or_404(self.queryset, pk=pk)
        assignment.delete()
        return Response({"message": "assignment deleted successfully"})
    
    
class RespondViews(viewsets.ModelViewSet):
    queryset = models.Respond.objects.all()
    serializer_class = serializers.RespondSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self,request):
        respond = models.Respond.objects.all()
        serailizer = serializers.RespondSerializer(respond, many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        respond = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.RespondSerializer(respond, pk=pk)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, requset):
        serializer = serializers.RespondSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, requset, pk=None):
        respond = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.RespondSerializer(respond,data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def partial_update(self, requset, pk=None):
        respond = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.RespondSerializer(respond,data=requset.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, requset, pk=None):
        respond = get_object_or_404(self.queryset, pk=pk)
        respond.delete()
        return Response({"message": "respond deleted successfully"})    


   
class AssignmentScoreViews(viewsets.ModelViewSet):
    queryset = models.AssignmentScore.objects.all()
    serializer_class = serializers.AssignmentScoreSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self,request):
        score = models.AssignmentScore.objects.all()
        serailizer = serializers.AssignmentScoreSerializer(score, many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        score = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.AssignmentScoreSerializer(score, pk=pk)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, requset):
        serializer = serializers.AssignmentScoreSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, requset, pk=None):
        score = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.AssignmentScoreSerializer(score,data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def partial_update(self, requset, pk=None):
        score = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.AssignmentScoreSerializer(score,data=requset.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, requset, pk=None):
        score = get_object_or_404(self.queryset, pk=pk)
        score.delete()
        return Response({"message": "Score deleted successfully"})    
        