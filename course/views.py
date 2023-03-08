from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from . import models
from . import serializers
from . import filters
from departments.models import Subject


# staff list create update delete file start

class CourseViews(viewsets.ModelViewSet):

    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    # permission_classes= [IsAuthenticated,]
    
    def list(self, request):
        search = request.query_params.get('search')
        order = request.query_params.get('order')
        paginator = PageNumberPagination()
        paginator.page_size=5
        title=''
        if search==None:
            search=''
        if order == None:
            title = 'title'
        elif order == 'desc':
            title = '-title'
                    
        course = models.Course.objects.distinct().filter(
            Q(title__icontains=search) |
            Q(subject__name__icontains=search)
        ).order_by(title)
        
        coursefilter = filters.CourseFilter(request.GET, queryset=course)
        pages = paginator.paginate_queryset(coursefilter.qs, request)
        
        serializer = serializers.CourseSerializer(pages, many=True)
        return paginator.get_paginated_response(serializer.data)


    def retrieve(self, request, pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseSerializer(course)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        course = get_object_or_404(self.queryset, pk=pk)
        course.delete()
        return Response({"message": "course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CourseStatusViews(viewsets.ModelViewSet):

    queryset = models.CourseStatus.objects.all()
    serializer_class = serializers.CourseStatusSerializer
    # permission_classes= [IsAuthenticated,]
    
    def list(self, request):
        serializer = serializers.CourseStatusSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        course_status = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseStatusSerializer(course_status)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.CourseStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        course_status = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseStatusSerializer(course_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        course_status = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseStatusSerializer(course_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        course_status = get_object_or_404(self.queryset, pk=pk)
        course_status.delete()
        return Response({"message": "status deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




class CourseDetailViews(viewsets.ModelViewSet):

    queryset = models.CourseDetail.objects.all()
    serializer_class = serializers.CourseDetailSerializer
    # permission_classes= [IsAuthenticated,]
    
    def list(self, request):
        serializer = serializers.CourseDetailSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        detail = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseDetailSerializer(detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.CourseDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk=None):
        detail = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseDetailSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        detail = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.CourseDetailSerializer(detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        detail = get_object_or_404(self.queryset, pk=pk)
        detail.delete()
        return Response({"message": "course detail deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CourseModuleViews(viewsets.ModelViewSet):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer
    # permission_classes = [IsAuthenticated,]
    
    def list(self, request):
        serializer = serializers.ModuleSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        module = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ModuleSerializer(module)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = serializers.ModuleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        module = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        module = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ModuleSerializer(module, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        module = get_object_or_404(self.queryset, pk=pk)
        module.delete()
        return Response({"message": "Course Module deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        

class CourseContentTypeViews(viewsets.ModelViewSet):
    queryset = models.ContentType.objects.all()
    serializer_class = serializers.ContentTypeSerializer
    # permission_classes = [IsAuthenticated,]
    
    def list(self, request):
        serializer = serializers.ContentTypeSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        contenttype = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ContentTypeSerializer(contenttype)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = serializers.ContentTypeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        contenttype = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ContentTypeSerializer(contenttype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        contenttype = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.ContentTypeSerializer(contenttype, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        contenttype = get_object_or_404(self.queryset, pk=pk)
        contenttype.delete()
        return Response({"message": "Course content type deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
                                    
        