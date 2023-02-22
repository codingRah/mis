from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.custom_serializers.students_serializers import StudentsSerializer, StudentHostelSerializer,StudentRelationContactSerializer, StudentStatusSerializer, StudentsCartSerializer
from apps.custom_models.students_models import Student, StudentHostelService, StudentNationlityCartInfo, StudentStatus,StudentRelationContact



class StudentViews(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes =  [IsAuthenticated]

    def list(self , request):
        serializer = StudentsSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        student = get_object_or_404(self.queryset,pk=None )
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.create)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request,pk=None):
        student = get_object_or_404(self.queryset, pk=None)
        serializer = StudentsSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=None)
        student.delete()
        return Response({"message" : "student deleted successfuly"})

class StudentStatus(viewsets.ModelViewSet):
    queryset = StudentStatus.objects.all()
    serializer_class = StudentStatusSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = StudentStatusSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        status = get_object_or_404(self.queryset, many=True)
        serializer = StudentStatusSerializer(status)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, pk=None):
        serializer = StudentStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        status = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentStatusSerializer(status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        status = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentStatusSerializer(status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        status = get_object_or_404(self.queryset,pk=pk)
        status.delete()
        return Response({"message": "status deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class StudentHostel(viewsets.ModelViewSet):
    queryset = StudentHostelService.objects.all()
    serializer_class = StudentHostelSerializer
    permission_classes = [IsAuthenticated]


    def list(self , request):
        serializer = StudentHostelSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        hostel = get_object_or_404(self.queryset, many=True)
        serializer = StudentHostelSerializer(hostel)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = StudentHostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        hostel = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentHostelSerializer(hostel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

    def partial_update(self, request, pk=None):
        hostel = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentHostelSerializer(hostel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        hostel = get_object_or_404(self.queryset, pk=pk)
        hostel.delete()
        return Response({"message":"hostel deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

