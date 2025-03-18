from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, TestUserSerializer

@api_view(['GET','POST'])
def user_api_views(request):
    # list
    if request.method == 'GET':
        #queryset
        users = User.objects.all()
        user_serializer = UserSerializer(users,many=True)
        
        return Response({
            'message': 'Lista de usuarios',
            'data': user_serializer.data
        }, status=status.HTTP_200_OK)

    #create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        #validations
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario creado correctamente',
                'data': user_serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Error al crear el usuario',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk):
    user = User.objects.filter(id=pk).first()
    #validations
    if user:
        #retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        

        # update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado correctamente'},status=status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado este usuario con estos datos'},status=status.HTTP_400_BAD_REQUEST)
