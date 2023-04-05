from . import serializers
from rest_framework.response import Response

from rest_framework.decorators import permission_classes , api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import Permission
from rest_framework.pagination import PageNumberPagination
from . import models
from accounts.models import User
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


# department list create update delete file start
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def department_list_create_view(request):
    data = request.data
    search = request.query_params.get("search")
    order = request.query_params.get("order")
    name = ""
    if search == None:
        search = ""
    if order == None:
        order == "asc"
    if order == "asc":
        name = "name"
    else:
        name = "-name"
    if request.method == 'GET':
        department = models.Department.objects.filter(name__icontains=search).order_by(name)
        serializer = serializers.DepartmentSerializer(department, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        name = data['name']
        description = data['description']
        code = data['code']
        created_at = data['created_at']

        department = models.Department.objects.create(
            name=name, 
            description=description, 
            code=code, 
            created_at=created_at
        )
        serializer = serializers.DepartmentSerializer(department, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def department_update_delete_view(request, slug):
    data = request.data
    if request.method == "GET":
        department = models.Department.objects.get(slug=slug)
        serializer = serializers.DepartmentSerializer(department)
        return Response(serializer.data)

    if request.method == 'PUT':
        name = data['name']
        description = data['description']
        code = data['code']
        created_at = data['created_at']
        department = models.Department.objects.get(slug=slug)
        department.name = name
        department.description = description
        department.code = code
        department.created_at = created_at
        department.save()
        
        serializer = serializers.DepartmentSerializer(department, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':        
        department = models.Department.objects.get(slug=slug)
        department.delete()
        return Response({'message': 'Successfully department deleted!!'}, status=status.HTTP_200_OK)


class DepartmentChiefView(viewsets.ModelViewSet):
    queryset = models.DepartmentChief.objects.all()
    serializer_class = serializers.DepartmentChiefSerilizer
    # authentication_classes = (IsAuthenticated, )
    def list(self, request):
        chief = models.DepartmentChief.objects.all()
        serializer = serializers.DepartmentChiefSerilizer(chief, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        chief = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.DepartmentChiefSerilizer(chief)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        department = data.get('department')
        user = data.get('user')
        from_date = data.get('from_date')
        to_date = data.get('to_date')
        try:
            department = models.Department.objects.get(id=department)
            user = User.objects.get(id=user)
        except:
            return Response({'error':'some data is not matched'})   
        chief_create = models.DepartmentChief.objects.create(
            department=department,
            user = user,
            from_date = from_date,
            to_date = to_date
        ) 
        print(chief_create)
        serializer = serializers.DepartmentChiefSerilizer(chief_create, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def update(self, request,pk=None):
        chief = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.DepartmentChiefSerilizer(chief, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        chief = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.DepartmentChiefSerilizer(chief, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        chief = get_object_or_404(self.queryset, pk=pk)
        chief.delete()
        return Response({"message": "Department chief deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




# department program level CRUD start
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def department_programlevel_list_create_view(request):
    data = request.data
    if request.method == 'GET':
        programlevel = models.DepartmentProgramLevel.objects.all()
        serializer = serializers.DepartmentProgramLevelSerializer(programlevel, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        department = data.get('department')
        level = data.get('level')
        try:
            department = models.Department.objects.get(id=department)
        except:
            return Response({'error':'some data is not matched'})   
        level_created = models.DepartmentProgramLevel.objects.create(
            department=department,
            level = level,
        ) 
        print(level_created)
        serializer = serializers.DepartmentProgramLevelSerializer(level_created, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def department_programlevel_update_delete_view(request, pk):
    if request.method == "GET":
        programlevel = models.DepartmentProgramLevel.objects.get(pk=pk)
        serializer = serializers.DepartmentProgramLevelSerializer(programlevel)
        return Response(serializer.data)
    if request.method == 'PUT':
        programlevel = models.DepartmentProgramLevel.objects.get(pk=pk)
        serializer = serializers.DepartmentProgramLevelSerializer(data=request.data, instance=programlevel)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':        
        programlevel = models.DepartmentProgramLevel.objects.get(pk=pk)
        programlevel.delete()
        return Response({'message': 'Successfully department progarm level deleted!!'}, status=status.HTTP_200_OK)
 
# end of department program level

# start of semester
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def semester_list_create_view(request):
    if request.method == 'GET':
        semester = models.Semester.objects.all()
        serializer = serializers.SemesterSerializer(semester, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def semester_update_delete_view(request, pk):
    if request.method == "GET":
        semester = models.Semester.objects.get(pk=pk)
        serializer = serializers.SemesterSerializer(semester)
        return Response(serializer.data)
    if request.method == 'PUT':
        semester = models.Semester.objects.get(pk=pk)
        serializer = serializers.SemesterSerializer(data=request.data, instance=semester)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':        
        semester = models.Semester.objects.get(pk=pk)
        semester.delete()
        return Response({'message': 'Successfully semester deleted!!'}, status=status.HTTP_200_OK)
 


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def subject_list_create_view(request):
    data = request.data
    

    if request.method == 'GET':
        query = request.query_params.get("query", "")
        sort_query = request.query_params.get('sort', {'order' : "asc", "key" : "name"})
        sort_query = eval(sort_query)
        pageSize = request.query_params.get("pageSize")

        paginator = PageNumberPagination()
        paginator.page_size = pageSize
        paginator.page_query_param = 'pageIndex'
        queryset = models.Subject.objects.all()
        if query:
            queryset = queryset.filter(name__icontains=query)
        if sort_query:
            sort_order = '-' if sort_query.get('order', "") == 'desc' else ''
            sort_field = sort_query.get('key', 'name')
            if sort_field in [f.name for f in models.Subject._meta.fields]:
                queryset = queryset.order_by(f"{sort_order}{sort_field}")
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = serializers.SubjectSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'POST':
        name = data['name']
        credit = data['credit']
        subject_type = data['subject_type']
        description = data['description']
        code = data['code']
        department = models.Department.objects.get(id=data['department']) 
        semester = models.Semester.objects.get(id=data['semester'])

        subject = models.Subject.objects.create(
            name=name, 
            credit = credit,
            subject_type = subject_type,
            description=description, 
            code=code, 
            department=department,
            semester =semester
        )
        serializer = serializers.SubjectSerializer(subject, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def subject_update_delete_view(request, slug):
    data = request.data
    if request.method == "GET":
        subject = models.Subject.objects.get(slug=slug)
        serializer = serializers.SubjectSerializer(subject)
        return Response(serializer.data)

    if request.method == 'PUT':
        name = data['name']
        credit = data['credit']
        subject_type = data['subject_type']
        description = data['description']
        code = data['code']
        department = models.Department.objects.get(id=data['department']) 
        semester = models.Semester.objects.get(id=data['semester'])

        subject = models.Subject.objects.get(slug=slug)
        subject.name = name
        subject.credit=credit
        subject.subject_type=subject_type
        subject.description = description
        subject.code = code
        subject.department = department
        subject.semester = semester
        subject.save()
        
        serializer = serializers.SubjectSerializer(subject, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':        
        subject = models.Subject.objects.get(slug=slug)
        subject.delete()
        return Response({'message': 'Successfully subject deleted!!'}, status=status.HTTP_200_OK)


 