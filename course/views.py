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
from students.models import Student
from staff.models import Staff
from rest_framework.decorators import action


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
        owner = request.data['owner']
        session = request.data['session']
        subject = request.data['subject']
        # student = request.data['student']
        code = request.data['code']
        title = request.data['title']
        description = request.data['description']
        
        try:
            owner = Staff.objects.get(id=owner)
            session = models.Session.objects.get(id=session)
            subject = Subject.objects.get(id=subject)
            # student = Student.objects.get(id=student)
        except:
            return Response({'error':'show related value is not matched'})    

        course_create = models.Course.objects.create(
            owner = owner,
            session = session,
            subject = subject,
            code = code,
            title = title,
            # student = student,
            description = description
        )
        serializer = serializers.CourseSerializer(course_create)
        course  = serializer.save()        
        return Response(course, status=status.HTTP_201_CREATED)
        
        
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
        course = request.data.get('course')
        status_course = request.data.get('status')
        try:
            course = models.Course.objects.get(id=course)
        except:
            return Response({'error':'some data is not matched'})   
        course_status = models.CourseStatus.objects.create(
            course=course,
            status = status_course
        ) 
        serializer = serializers.CourseStatusSerializer(course_status)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
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
        course = request.data.get('course')
        image = request.data.get('image')
        color = request.data.get('color')
        try:
            course = models.Course.objects.get(id=course)
        except:
            return Response({'error':'some data is not matched'})   
        course_detail = models.CourseDetail.objects.create(
            course=course,
            image = image,
            color = color,
        ) 
        serializer = serializers.CourseDetailSerializer(course_detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
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
        course = request.data.get('course')
        week = request.data.get('week')
        description = request.data.get('description')
        title = request.data.get('title')
        try:
            course = models.Course.objects.get(id=course)
        except:
            return Response({'error':'some data is not matched'})   
        course_detail = models.Module.objects.create(
            course=course,
            week = week,
            description = description,
            title = title
        ) 
        serializer = serializers.ModuleSerializer(course_detail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
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
        
class CourseEventViews(viewsets.ModelViewSet):
    queryset = models.CourseEvent.objects.all()
    serializer_class = serializers.CourseEventSerializer
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        event = models.CourseEvent.objects.all()
        serializer = serializers.CourseEventSerializer(event,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.CourseEventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        course = request.data.get('course')
        end_at = request.data.get('end_at')
        description = request.data.get('description')
        title = request.data.get('title')
        try:
            course = models.Course.objects.get(id=course)
        except:
            return Response({'error':'some data is not matched'})   
        event = models.CourseEvent.objects.create(
            course=course,
            end_at = end_at,
            description = description,
            title = title
        ) 
        serializer = serializers.CourseEventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def update(self,requset, pk=None):
        event = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.CourseEventSerializer(event, data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def parial_padate(self, request, pk=None):
        event = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.CourseEventSerializer(event,data=request.data, parial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request, pk=None):
        event = get_object_or_404(self.queryset,pk=pk)
        event.delete()
        return Response({"message": "course event deleted"}, status=status.HTTP_204_NO_CONTENT)
    

class CourseContentViews(viewsets.ModelViewSet):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self,request):
        content = models.Content.objects.all()
        serializer = serializers.ContentSerializer(content,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        content = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ContentSerializer(content)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def create(self, request):
        module = request.data.get('module')
        description = request.data.get('description')
        title = request.data.get('title')
        try:
            module = models.Module.objects.get(id=module)
        except:
            return Response({'error':'some data is not matched'})   
        module_create = models.Content.objects.create(
            module=module,
            description = description,
            title = title
        ) 
        serializer = serializers.ContentSerializer(module_create)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def update(self,requset, pk=None):
        content = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ContentSerializer(content, data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def parial_padate(self, request, pk=None):
        content = get_object_or_404(self.queryset,pk=pk)
        serializer = serializers.ContentSerializer(content,data=request.data, parial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request, pk=None):
        content = get_object_or_404(self.queryset,pk=pk)
        content.delete()
        return Response({"message": "course content deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
          

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
        content = request.data.get('content')
        url = request.data.get('url')
        file = request.data.get('file')
        image = request.data.get('image')
        try:
            content = models.Content.objects.get(id=content)
        except:
            return Response({'error':'some data is not matched'})   
        content_type = models.ContentType.objects.create(
            content=content,
            url = url,
            file = file,
            image = image
        ) 
        serializer = serializers.ContentTypeSerializer(content_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    
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
                                    

class CourseSessionViews(viewsets.ModelViewSet):
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
    # permission_classes = [IsAuthenticated,]
    
    def list(self, request):
        session = models.Session.objects.all()
        serializer = serializers.SessionSerializer(session, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        session = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.SessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = serializers.SessionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def update(self, request, pk=None):
        session = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        session = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.SessionSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None):
        session = get_object_or_404(self.queryset, pk=pk)
        session.delete()
        return Response({"message": "Course Session deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
                                                                        


class SubjectAssignmentToInstructorViews(viewsets.ModelViewSet):

    queryset = models.SubjectAssignmentToInstructor.objects.all()
    serializer_class = serializers.SubjectAssignmentToInstructorSerializer
    # permission_classes= [IsAuthenticated,]
    
    def list(self, request):
        sub_instructor = models.SubjectAssignmentToInstructor.objects.all()
        serializer = serializers.SubjectAssignmentToInstructorSerializer(sub_instructor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        sub_instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.SubjectAssignmentToInstructorSerializer(sub_instructor)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        session = request.data['session']
        instructor = request.data['instructor']
        subject = request.data['subject']
        semester = request.data['semester']
        
        try:
            instructor = Staff.objects.get(id=instructor)
            session = models.Session.objects.get(id=session)
            subject = Subject.objects.get(id=subject)
            semester = models.Semester.objects.get(id=semester)
        except:
            return Response({'error':'show related value is not matched'})    

        assignment_to_instructor = models.SubjectAssignmentToInstructor.objects.create(
            instructor = instructor,
            session = session,
            subject = subject,
            semester = semester
        )
        serializer = serializers.SubjectAssignmentToInstructorSerializer(assignment_to_instructor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        


    def update(self, request,pk=None):
        sub_instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.SubjectAssignmentToInstructorSerializer(sub_instructor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        sub_instructor = get_object_or_404(self.queryset, pk=pk)
        serializer = serializers.SubjectAssignmentToInstructorSerializer(sub_instructor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        sub_instructor = get_object_or_404(self.queryset, pk=pk)
        sub_instructor.delete()
        return Response({"message": "subject assing to instructor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

