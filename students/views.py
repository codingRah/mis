from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer, StudentHostelSerializer,StudentRelationContactSerializer, StudentStatusSerializer, StudentsCartSerializer
from .models import Student, StudentHostelService, StudentNationlityCartInfo, StudentStatus,StudentRelationContact
from django_filters.rest_framework import DjangoFilterBackend
from .filters import StudentFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import StudentPagination
from rest_framework import filters


class StudentViews(viewsets.ModelViewSet):

    """view for students"""

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    pagination_class = StudentPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = StudentFilter
    search_fields = ["kankor_id","first_name","last_name"]
    ordering_fields = ["first_name"]
    permission_classes = (IsAuthenticated,)

    # def list(self, request):
    #     student = Student.objects.all()
    #     serializer = StudentSerializer(student, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        student.delete()
        return Response({"message": "Student deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class StudentStatusViews(viewsets.ModelViewSet):

    """view for students Status"""
    serializer_class = StudentStatusSerializer
    queryset = StudentStatus.objects.all()
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        student_status = StudentStatus.objects.all()
        serializer = StudentStatusSerializer(student_status, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        student_status = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentStatusSerializer(student_status)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        student_status = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentStatusSerializer(student_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student_status = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentStatusSerializer(student_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student_status = get_object_or_404(self.queryset, pk=pk)
        student_status.delete()
        return Response({"message": "student status deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class StudentRelationContactViews(viewsets.ModelViewSet):

    """view for students contact"""
    serializer_class = StudentRelationContactSerializer
    queryset = StudentRelationContact.objects.all()
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        student_contact = StudentRelationContact.objects.all()
        serializer = StudentRelationContactSerializer(student_contact, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        student_contact = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentRelationContactSerializer(student_contact)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentRelationContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        student_contact = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentRelationContactSerializer(student_contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student_contact = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentRelationContactSerializer(student_contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student_contact = get_object_or_404(self.queryset, pk=pk)
        student_contact.delete()
        return Response({"message": "student contact deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class StudentHostelViews(viewsets.ModelViewSet):

    """view for students hostel"""
    serializer_class = StudentHostelSerializer
    queryset = StudentHostelService.objects.all()
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        student_hostel = StudentHostelService.objects.all()
        serializer = StudentHostelSerializer(student_hostel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        student_hostel = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentHostelSerializer(student_hostel)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentHostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        student_hostel = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentHostelSerializer(student_hostel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student_hostel = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentHostelSerializer(student_hostel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student_hostel = get_object_or_404(self.queryset, pk=pk)
        student_hostel.delete()
        return Response({"message": "student hostel deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class StudentCartInfolViews(viewsets.ModelViewSet):

    """view for students Info"""
    serializer_class = StudentsCartSerializer
    queryset = StudentNationlityCartInfo.objects.all()
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        student_cart = StudentNationlityCartInfo.objects.all()
        serializer = StudentsCartSerializer(student_cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        student_cart = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsCartSerializer(student_cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentsCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        student_cart = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsCartSerializer(student_cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student_cart = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsCartSerializer(student_cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student_cart = get_object_or_404(self.queryset, pk=pk)
        student_cart.delete()
        return Response({"message": "student cart info deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
