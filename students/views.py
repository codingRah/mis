from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentsSerializer, StudentHostelSerializer,StudentRelationContactSerializer, StudentStatusSerializer, StudentsCartSerializer
from .models import Student, StudentHostelService, StudentNationlityCartInfo, StudentStatus,StudentRelationContact
from django_filters.rest_framework import DjangoFilterBackend
from .filters import StudentFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import StudentPagination
from rest_framework import filters

class StudentViews(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes =  [IsAuthenticated,]
    pagination_class = StudentPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    filterset_class = StudentFilter
    search_fields = ["kankor_id","first_name","last_name"]
    ordering_fields = ["first_name"]
    
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentsSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        student = get_object_or_404(self.queryset,pk=pk)
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request,pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        student.delete()
        return Response({"message" : "student deleted successfuly"})
# @api_view(['GET'])
# def statuslist(request):
#     st_status = StudentStatus.objects.all()
#     serializer = StudentStatusSerializer(st_status, many=True)
#     return Response(serializer.data)

class StudentStatusView(viewsets.ModelViewSet):
    queryset = StudentStatus.objects.all()
    serializer_class = StudentStatusSerializer
    
    
    def list(self, request):
        queryset = StudentStatus.objects.all()
        serializer = StudentStatusSerializer(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        st_status = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentStatusSerializer(st_status)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        st_status = get_object_or_404(self.queryset,pk=pk)
        serializer = StudentStatusSerializer(st_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request,pk=None):
        st_status = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentStatusSerializer(st_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk=None):
        st_status = get_object_or_404(self.queryset, pk=pk)
        st_status.delete()
        return Response({"message" : "student deleted successfuly"})


class StudentHostelView(viewsets.ModelViewSet):
    queryset = StudentHostelService.objects.all()
    serializer_class = StudentHostelSerializer
    permission_classes = [IsAuthenticated,]


    def list(self , request):
        serializer = StudentHostelSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        hostel = get_object_or_404(self.queryset, many=True)
        serializer = StudentHostelSerializer(hostel)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = StudentHostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        hostel = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentHostelSerializer(hostel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

    def partial_update(self, request, pk=None):
        hostel = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentHostelSerializer(hostel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        hostel = get_object_or_404(self.queryset, pk=pk)
        hostel.delete()
        return Response({"message":"hostel deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class StudentRelationContactView(viewsets.ModelViewSet):
    queryset = StudentRelationContact.objects.all()
    serializer_class = StudentRelationContactSerializer
    permission_classes = [IsAuthenticated,]

    def list(self,request):
        serializer = StudentRelationContactSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        contact = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentRelationContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentRelationContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, {"message" : "contact is not created"})
        
    def update(self, request, pk=None):
        contact  = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentRelationContactSerializer(contact , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, {"message" : "contact is not updated"})
        

    def partial_update(self, request, pk=None):
        contact  = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentRelationContactSerializer(contact , data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, {"message" : "contact is not updated"})
        
    def destroy(self, request, pk=None):
        contact  = get_object_or_404(self.queryset, pk=pk)
        contact.delete()
        return Response({"message": "relation contact is deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    


class StudentCartInfoView(viewsets.ModelViewSet):
    queryset = StudentNationlityCartInfo.objects.all()
    serializer_class = StudentsCartSerializer
    permission_classes = [IsAuthenticated,]

    def list(self,request):
        serializer = StudentsCartSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        cartinfo = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsCartSerializer(cartinfo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentsCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, {"message" : "cartinfo is not created"})
        
    def update(self, request, pk=None):
        cartinfo  = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsCartSerializer(cartinfo , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, {"message" : "cartinfo is not updated"})
        

    def partial_update(self, request, pk=None):
        cartinfo  = get_object_or_404(self.queryset, pk=pk)
        serializer = StudentsCartSerializer(cartinfo , data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, {"message" : "cartinfo is not updated"})
        
    def destroy(self, request, pk=None):
        cartinfo  = get_object_or_404(self.queryset, pk=pk)
        cartinfo.delete()
        return Response({"message": "relation cartinfo is deleted successfully"},status=status.HTTP_204_NO_CONTENT)


