from django.shortcuts import render
from rest_framework import viewsets
from . models import Client, Project , User
from . serializers import clientserializer, projectserializer, userserializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

# client viewsets

class clientviewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = clientserializer


    #clinets/{client_id}/projects

    @action(detail = True , methods = ["get"])
    def projects(self,  request, pk = None):

        try:
            client = Client.objects.get(pk = pk)
            project = Project.objects.filter(client= client)
            pro_serializer = projectserializer(project, many = True, context = {'request':request})
            return Response(pro_serializer.data)
        
        except Exception as e:
            print(e)
            return Response({
                'message':"client might not exists"
            })




# project viewset

class projectviewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = projectserializer


# user viewset

class userviewset( viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer 