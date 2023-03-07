from django.shortcuts import render
from .serializers import UserSerializer, UserTypeSerializer, PermissionSerializer, UserAddressSerializer, UserSerializerWithToken
from .models import User, UserType, UserAddress
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes , api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attr):
        data = super().validate(attr)
        serializer = UserSerializerWithToken(self.user).data

        for key, value in serializer.items():
            if key == 'is_active' and value == False:
                return False
            data[key] = value
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def user_list_create_view(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data  = request.data
        username = data["username"]
        email = data["email"]
        password = data["password"]
        re_password = data["re_password"]
        user_type = data["user_type"]
        if User.objects.filter(email=email).exists():
            return Response({"message" : "User with this email already exists "}, status=status.HTTP_400_BAD_REQUEST)
        elif User.objects.filter(username=username).exists():
            return Response({"message" : "User with this username already exists "}, status=status.HTTP_400_BAD_REQUEST)
        elif len(username) < 3:
            return Response({"message" : "Username should contais at least 3 characters "},status=status.HTTP_400_BAD_REQUEST)

        elif password != re_password:
            return Response({
                "message" : "Passwords do not match "
            },status=status.HTTP_400_BAD_REQUEST)
        elif len(password) < 6:
            return Response({
                "message" : "A strong password contains at least 6 characters "
            },status=status.HTTP_400_BAD_REQUEST)

        else:
            user  = User.objects.create_user(
                email=email, 
                username=username,
                password=password
            )
            for t in user_type:
                u_type = UserType.objects.get(id=t)
                user.user_type.add(u_type)
                user.save()
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)

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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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

