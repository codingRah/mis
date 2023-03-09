from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import permission_classes , api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import Permission
from . import models


# department list create update delete file start
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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

# department create upadate ... end


# department Chief CRUD start
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def department_chief_list_create_view(request):
    if request.method == 'GET':
        chief = models.DepartmentChief.objects.all()
        serializer = serializers.DepartmentChiefSerilizer(chief, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.DepartmentChiefSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def department_chief_update_delete_view(request, pk):
    if request.method == "GET":
        chief = models.DepartmentChief.objects.get(pk=pk)
        serializer = serializers.DepartmentChiefSerilizer(chief)
        return Response(serializer.data)
    if request.method == 'PUT':
        chief = models.DepartmentChief.objects.get(pk=pk)
        serializer = serializers.DepartmentChiefSerilizer(data=request.data, instance=chief)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':        
        chief = models.DepartmentChief.objects.get(pk=pk)
        chief.delete()
        return Response({'message': 'Successfully department chief deleted!!'}, status=status.HTTP_200_OK)
    
# end of department 

# department program level CRUD start
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def department_programlevel_list_create_view(request):
    if request.method == 'GET':
        programlevel = models.DepartmentProgramLevel.objects.all()
        serializer = serializers.DepartmentProgramLevelSerializer(programlevel, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.DepartmentProgramLevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)


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
        subject = models.Subject.objects.filter(name__icontains=search).order_by(name)
        serializer = serializers.SubjectSerializer(subject, many=True)
        return Response(serializer.data)
    
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


 