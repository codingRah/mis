from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from . import models
from . import serializers
from . import pagination
from . import filters


# staff list create update delete file start

class InstructorViews(viewsets.ModelViewSet):

    queryset = models.Staff.objects.all()
    serializer_class = serializers.InstructorSerializer
    pagination_class = pagination.InstructorPaginator       
    permission_classes =  [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = filters.StaffFilter
    search_fields = ["first_name",'last_name']
    ordering_fields = ["first_name"]

    def retrieve(self, request, pk=None):
        instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorSerializer(instructor)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorSerializer(instructor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorSerializer(instructor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        instructor = get_object_or_404(self.queryset, pk=pk)
        instructor.delete()
        return Response({"message": "instructor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class InstructorCartViews(viewsets.ModelViewSet):

    queryset = models.StaffNationlityCartInfo.objects.all()
    serializer_class = serializers.InstructorNationalityCartInfoSerializer
    permission_classes =  [IsAuthenticated,]

    def list(self, request):
        serializer = serializers.InstructorNationalityCartInfoSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorNationalityCartInfoSerializer(cart)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.InstructorNationalityCartInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorNationalityCartInfoSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorNationalityCartInfoSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        cart = get_object_or_404(self.queryset, pk=pk)
        cart.delete()
        return Response({"message": "cart deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class InstructorEducationViews(viewsets.ModelViewSet):
    queryset = models.StaffEducation.objects.all()
    serializer_class = serializers.InstructorEductionSerializer
    permission_classes = [IsAuthenticated,]


    def list(self, request):
        serializer = serializers.InstructorEductionSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        education = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorEductionSerializer(education)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.InstructorEductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, {"message": "education is not created"})


    def update(self, request, pk=None):
        education = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.InstructorEductionSerializer(education, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        education = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorEductionSerializer(education, data=request.data, partial=True)
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
    queryset = models.StaffJobExperience.objects.all()
    serializer_class = serializers.InstructorExperienceSerializer
    permission_classes= [IsAuthenticated,]


    def list(self, request):
        serializer = serializers.InstructorExperienceSerializer(self.queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        experience = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorExperienceSerializer(experience)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.InstructorExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        experience = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorExperienceSerializer(experience, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        experience = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorExperienceSerializer(experience, data=request.data, parial=True)
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
    queryset = models.StaffExtraInfo.objects.all()
    serializer_class = serializers.InstructorExtraInfoSerializer
    permission_classes= [IsAuthenticated,]


    def list(self, request):
        serializer = serializers.InstructorExtraInfoSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        extraInfo = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorExtraInfoSerializer(extraInfo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.InstructorExtraInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        extraInfo = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorExtraInfoSerializer(extraInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        extraInfo = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.InstructorExtraInfoSerializer(extraInfo, data=request.data, parial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        extraInfo = get_object_or_404(self.queryset, pk=pk)
        extraInfo.delete()
        return Response({"message": "extraInfo deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
