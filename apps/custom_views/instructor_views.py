from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.custom_models import instructors_models
from django.db.models import Q
from rest_framework import viewsets
from apps.custom_serializers import instructor_serializers
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.filters.filters import StaffFilter
from rest_framework.filters import SearchFilter,OrderingFilter


# staff list create update delete file start

class InstructorViews(viewsets.ModelViewSet):

    queryset = instructors_models.Staff.objects.all()
    serializer_class = instructor_serializers.InstructorSerializer
    # permission_classes =  [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = StaffFilter
    search_fields = ["first_name","last_name"]
    ordering_fields = ["first_name"]
    
    # def list(self, request):
       
        # data = request.data
        # search = request.query_params.get("search")
        # order = request.query_params.get("order")
        # first_name = ""
        
        # if search == None:
        #     search = ""
        # if order == None:
        #     order == "asc"
        # if order == "desc":
        #     first_name = "first_name"
         
        # else:
        #     first_name = "-first_name"
           

        # staff = instructors_models.Staff.objects.filter(
        #     Q(first_name__icontains=search) |
        #     Q(gender__icontains=search)|
        #     Q(department__name__icontains=search)).order_by(first_name)
        # staff = instructors_models.Staff.objects.all()

        # serializer = instructor_serializers.InstructorSerializer(self.queryset, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorSerializer(instructor)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = instructor_serializers.InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorSerializer(instructor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorSerializer(instructor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        instructor = get_object_or_404(self.queryset, pk=pk)
        instructor.delete()
        return Response({"message": "instructor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class InstructorCart(viewsets.ModelViewSet):

    queryset = instructors_models.StaffNationlityCartInfo.objects.all()
    serializer_class = instructor_serializers.InstructorNationalityCartInfoSerializer
    permission_classes =  [IsAuthenticated,]

    def list(self, request):
        serializer = instructor_serializers.InstructorNationalityCartInfoSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorNationalityCartInfoSerializer(cart)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = instructor_serializers.InstructorNationalityCartInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorNationalityCartInfoSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorNationalityCartInfoSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        cart.delete()
        return Response({"message": "cart deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class InstructorEducation(viewsets.ModelViewSet):
    queryset = instructors_models.StaffEducation.objects.all()
    serializer_class = instructor_serializers.InstructorEductionSerializer
    permission_classes = [IsAuthenticated,]


    def list(self, request):
        serializer = instructor_serializers.InstructorEductionSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        education = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorEductionSerializer(education)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = instructor_serializers.InstructorEductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, {"message": "education is not created"})


    def update(self, request, pk=None):
        education = get_object_or_404(self.queryset,pk=pk)
        serializer = instructor_serializers.InstructorEductionSerializer(education, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        education = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorEductionSerializer(education, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        education = get_object_or_404(self.queryset, pk=pk)
        education.delete()
        return Response({"message": "education deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)


class InstructorExperience(viewsets.ModelViewSet):
    queryset = instructors_models.StaffJobExperience.objects.all()
    serializer_class = instructor_serializers.InstructorExperienceSerializer
    permission_classes= [IsAuthenticated,]


    def list(self, request):
        serializer = instructor_serializers.InstructorExperienceSerializer(self.queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        experience = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorExperienceSerializer(experience)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = instructor_serializers.InstructorExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        experience = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorExperienceSerializer(experience, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        experience = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorExperienceSerializer(experience, data=request.data, parial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        experience = get_object_or_404(self.queryset, pk=pk)
        experience.delete()
        return Response({"message": "experience deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class InstructorExtraInfo(viewsets.ModelViewSet):
    queryset = instructors_models.StaffExtraInfo.objects.all()
    serializer_class = instructor_serializers.InstructorExtraInfoSerializer
    permission_classes= [IsAuthenticated,]


    def list(self, request):
        serializer = instructor_serializers.InstructorExtraInfoSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        extraInfo = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorExtraInfoSerializer(extraInfo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = instructor_serializers.InstructorExtraInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        extraInfo = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorExtraInfoSerializer(extraInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        extraInfo = get_object_or_404(self.queryset, pk=pk)
        serializer = instructor_serializers.InstructorExtraInfoSerializer(extraInfo, data=request.data, parial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        extraInfo = get_object_or_404(self.queryset, pk=pk)
        extraInfo.delete()
        return Response({"message": "extraInfo deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
