from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer,StudentBulkUploadSerializer, StudentHostelSerializer,StudentRelationContactSerializer, StudentStatusSerializer, StudentsCartSerializer
from .models import Student,StudentBulkUpload, StudentHostelService, StudentNationlityCartInfo, StudentStatus,StudentRelationContact
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from .filters import StudentFilter
from django_filters.utils import translate_validation


class StudentViews(viewsets.ModelViewSet):

    """view for students"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = (IsAuthenticated,)
   

    def list(self, request):
       
        search = request.query_params.get("search")
        order = request.query_params.get("order")
        paginator = PageNumberPagination()
        paginator.page_size = 2
        first_name = ""
        if search == None:
            search = ""
        if order == None:
            first_name = "first_name"
        if order == "desc":
            first_name = "-first_name"
        student = Student.objects.distinct().filter(
            Q(first_name__icontains=search)|
            Q(kankor_id__icontains=search)|
            Q(gender__icontains=search)|
            Q(department__name__icontains=search)
            ).order_by(first_name)
        filterset = StudentFilter(request.GET, queryset=student)
        if not filterset.is_valid():
            raise translate_validation(filterset.errors)
        pages = paginator.paginate_queryset(filterset.qs, request)
        serializer = StudentSerializer(pages, many=True)
        return paginator.get_paginated_response(serializer.data)
    
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


@api_view(['GET','POST'])
def student_bulk_upload_view(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        print(file, "hello")
        bulk_upload = StudentBulkUpload.objects.create(
            csv_file=file
        )
        print(bulk_upload, "builk here ")
        if bulk_upload:
            return Response({"message":"file uploaded"})
        else:
            return Response({"message":"file not uploaded "})
