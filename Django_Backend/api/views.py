from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint' : '/Django_Project/',
            'method' : 'GET',
            'username' : None,
            'password' : None,
            'ID' : None,
            'description' : 'Returns idk what but we will know soon'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getUsers(request):
    User = user.objects.all()
    serializer = userSerializer(User,many=True)
    return Response(serializer.data)

@api_view(['GET'])#GET FOR RETRIEVE 
def getSingleUser(request,uname):
    User = user.objects.filter(username=uname)
    serializer = userSerializer(User,many=False)
    return Response(serializer.data)

@api_view(['POST'])#POST FOR ADD
def createUser(request):
    data = request.data
    print(data)
    tempU = str(data['username'])
    tempU = tempU.lower()
    User = user.objects.create(
        username = tempU,
        password = data['password'],
    )
    serializer = userSerializer(User,many = False)
    return Response(serializer.data)