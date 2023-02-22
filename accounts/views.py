from django.shortcuts import render
from .serializers import UserSerializer, UserTypeSerializer, PermissionSerializer, UserAddressSerializer
from .models import User, UserType, UserAddress
from rest_framework.response import Response
from rest_framework.decorators import permission_classes , api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import Permission


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def user_list_create_view(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_update_delete_view(request, pk):
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'PUT':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(data=request.data, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'success': "user deleted successfully"},status=status.HTTP_200_OK)



@api_view(['GET','POST'])
@permission_classes(IsAuthenticated,)
def usertype_list_create_view(request):
    if request.method == 'GET':
        usertype = UserType.objects.all()
        serializer = UserTypeSerializer(usertype, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes(IsAuthenticated,)
def usertype_update_delete_view(request, pk):
    if request.method == 'GET':
        usertype = UserType.objects.get(pk=pk)
        serializer = UserTypeSerializer(usertype)
        return Response(serializer.data)

    if request.method == 'PUT':
        usertype = UserType.objects.get(pk=pk)
        serializer = UserTypeSerializer(data=request.data, instance=usertype)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        usertype = UserType.objects.get(pk=pk)
        usertype.delete()
        return Response({'success': "user type deleted successfully"},status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes(IsAuthenticated,)
def permission_list_views(request):
   
    permission = Permission.objects.all()
    serializer = PermissionSerializer(permission, many=True)
    return Response(serializer.data)



@api_view(['GET','POST'])
@permission_classes(IsAuthenticated,)
def useraddress_list_create_view(request):
    if request.method == 'GET':
        address = UserAddress.objects.all()
        serializer = UserAddressSerializer(address, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes(IsAuthenticated,)
def useraddress_update_delete_view(request, pk):
    if request.method == 'GET':
        address = UserAddress.objects.get(pk=pk)
        serializer = UserAddressSerializer(address)
        return Response(serializer.data)

    if request.method == 'PUT':
        address = UserAddress.objects.get(pk=pk)
        serializer = UserAddressSerializer(data=request.data, instance=address)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        address = UserAddress.objects.get(pk=pk)
        address.delete()
        return Response({'success': "useraddress deleted successfully"},status=status.HTTP_200_OK)

