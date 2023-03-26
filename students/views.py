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
import ast
from results.models import Result,Course
from departments.models import Subject  
from accounts.models import User


class StudentViews(viewsets.ModelViewSet):

    """view for students"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)
   

    def list(self, request):
        paginator = PageNumberPagination()

        paginator.page_size = 5
        query = request.query_params.get("query")
        department = request.query_params.get("department")
        sort_query = request.query_params.get('sort', {'order' : "asc", "key" : "name"})
        sort_query = eval(sort_query)
        pageSize = request.query_params.get("pageSize")
       
        paginator = PageNumberPagination()
        paginator.page_size = pageSize
        paginator.page_query_param = 'pageIndex'
        
        queryset = Student.objects.distinct().filter(
            Q(first_name__icontains=query)|
            Q(kankor_id__icontains=query)|
            Q(gender__icontains=query)
        )
        
        if sort_query:
            sort_order = '-' if sort_query.get('order', "") == 'desc' else ''
            sort_field = sort_query.get('key', 'name')
            if sort_field in [f.name for f in Student._meta.fields]:
                queryset = queryset.order_by(f"{sort_order}{sort_field}")
        
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = StudentSerializer(paginated_queryset, many=True)
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
        
        bulk_upload = StudentBulkUpload.objects.create(
            csv_file=file
        )
        
        if bulk_upload:
            return Response({"message":"file uploaded"})
        else:
            return Response({"message":"file not uploaded "})


@api_view(['GET'])
def semester_report_view(request, pk):
    student = Student.objects.get(pk=pk)
    results = []
    for result in Result.objects.all():
        if result.student == student and result.subject.semester == student.semester:
            results.append(result)
    subjects = Subject.objects.filter(department=student.department, semester=student.semester)
    
    my_courses = Course.objects.filter(students=student)
    # drawing charts for results
    courses = []
    score = []

    for result in results:
        if result.subject.semester == student.semester:
            courses.append(result.subject.subject)
            score.append(int(result.total_score()))
    
    total_credits = 0
    scores = 0
    percentage = 0
    passed_credits = 0
    grade = "D"

    for subject in subjects:
        total_credits += subject.credit

    for result in results:
        if result.subject.semester.semester_name == result.student.semester.semester_name:
            scores += result.total_score()
            if result.total_score() > 55:
                passed_credits += result.subject.credit
            if result.total_score() >= 55:
                result.is_pass = True
            else:
                result.is_pass = False
            result.save()    
    if passed_credits > (total_credits // 2) and student.semester.semester_number != 8:
        student.semester.semester_number += 1

        for course in my_courses:
            course.students.remove(student)
        student.save()
    try:
        percentage = scores / total_credits
    except:
        percentage = 0

    status = "ناکام"
    for r in results:
        if r.total_score() < 55:
            status = "چانس"
            break
        else:
            status = "کامیاب"
    if passed_credits < (total_credits // 2):
        status = "ناکام"
    
    if percentage < 55:
        grade = "F"
    elif percentage >= 55 or percentage <= 69:
        grade = "D"
    elif percentage >= 70 or percentage <= 79:
        grade = "C"
    elif percentage >= 80 or percentage <= 89:
        grade = "B"
    elif percentage >= 90 or percentage <= 100:
        grade = "A"
    # context = {
    #     "results": results,
    #     "student": student," total_credits": total_credits,"scores":scores," percentage":percentage,"passed_credits": passed_credits,"grade":grade,"score":score,"courses":courses,"status":status
    # }
    return 