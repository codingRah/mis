from apps.custom_serializers import departments_serializers
from rest_framework.response import Response
from rest_framework.decorators import permission_classes , api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import Permission
from apps.custom_models import departments_models

# department list create update delete file start
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def department_list_create_view(request):
    data = request.data
    if request.method == 'GET':
        department = departments_models.Department.objects.all()
        serializer = departments_serializers.DepartmentSerializer(department, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        name = data['name']
        description = data['description']
        code = data['code']
        created_at = data['created_at']

        print(created_at)

        department = departments_models.Department.objects.create(
            name=name,
            description=description,
            code=code,
            created_at=created_at
        )
        serializer = departments_serializers.DepartmentSerializer(department,many=False)
        return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes(IsAuthenticated,)
def department_update_delete_view(request, pk):
    if request.method == "GET":
        department = departments_models.Department.objects.get(pk=pk)
        serializer = departments_serializers.DepartmentSerializer(department)
        return Response(serializer.data)
    if request.method == 'PUT':
        department = departments_models.Department.objects.get(pk=pk)
        serializer = departments_serializers.DepartmentSerializer(data=request.data, instance=department)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':        
        department = departments_models.Department.objects.get(pk=pk)
        department.delete()
        return Response({'message': 'Successfully department deleted!!'}, status=status.HTTP_200_OK)

# department create upadate ... end


# department Chief CRUD start
@api_view(['GET', 'POST'])
def department_chief_list_create_view(request):
    if request.method == 'GET':
        chief = departments_models.DepartmentChief.objects.all()
        serializer = departments_serializers.DepartmentChiefSerilizer(chief, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = departments_serializers.DepartmentChiefSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes(IsAuthenticated,)
def department_chief_update_delete_view(request, pk):
    if request.method == "GET":
        chief = departments_models.DepartmentChief.objects.get(pk=pk)
        serializer = departments_serializers.DepartmentChiefSerilizer(chief)
        return Response(serializer.data)
    if request.method == 'PUT':
        chief = departments_models.DepartmentChief.objects.get(pk=pk)
        serializer = departments_serializers.DepartmentChiefSerilizer(data=request.data, instance=chief)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':        
        chief = departments_models.DepartmentChief.objects.get(pk=pk)
        chief.delete()
        return Response({'message': 'Successfully department chief deleted!!'}, status=status.HTTP_200_OK)
    
# end of department 

# department program level CRUD start
@api_view(['GET', 'POST'])
# @permission_classes(IsAuthenticated,)
def department_programlevel_list_create_view(request):
    if request.method == 'GET':
        programlevel = departments_models.DepartmentProgramLevel.objects.all()
        serializer = departments_serializers.DepartmentProgramLevelSerializer(programlevel, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = departments_serializers.DepartmentProgramLevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes(IsAuthenticated,)
def department_programlevel_update_delete_view(request, pk):
    if request.method == "GET":
        programlevel = departments_models.DepartmentProgramLevel.objects.get(pk=pk)
        serializer = departments_serializers.DepartmentProgramLevelSerializer(programlevel)
        return Response(serializer.data)
    if request.method == 'PUT':
        programlevel = departments_models.DepartmentProgramLevel.objects.get(pk=pk)
        serializer = departments_serializers.DepartmentProgramLevelSerializer(data=request.data, instance=programlevel)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':        
        programlevel = departments_models.DepartmentProgramLevel.objects.get(pk=pk)
        programlevel.delete()
        return Response({'message': 'Successfully department progarm level deleted!!'}, status=status.HTTP_200_OK)
 
# end of department program level

# start of semester
@api_view(['GET', 'POST'])
# @permission_classes(IsAuthenticated,)
def semester_list_create_view(request):
    if request.method == 'GET':
        semester = departments_models.Semester.objects.all()
        serializer = departments_serializers.SemesterSerializer(semester, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = departments_serializers.SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes(IsAuthenticated,)
def semester_update_delete_view(request, pk):
    if request.method == "GET":
        semester = departments_models.Semester.objects.get(pk=pk)
        serializer = departments_serializers.SemesterSerializer(semester)
        return Response(serializer.data)
    if request.method == 'PUT':
        semester = departments_models.Semester.objects.get(pk=pk)
        serializer = departments_serializers.SemesterSerializer(data=request.data, instance=semester)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':'data is not valid!!'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':        
        semester = departments_models.Semester.objects.get(pk=pk)
        semester.delete()
        return Response({'message': 'Successfully semester deleted!!'}, status=status.HTTP_200_OK)
 

      

 