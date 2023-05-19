from rest_framework import serializers
from . models import Client, Project, User


# creating  serializer for clinet

class clientserializer(serializers.HyperlinkedModelSerializer):
    client_id = serializers.ReadOnlyField()
    class Meta:
        model = Client
        fields =  "__all__"

# creating  serializer for user

class userserializer(serializers.HyperlinkedModelSerializer):

    user_id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = "__all__"


# creating  serializer for project

class projectserializer(serializers.HyperlinkedModelSerializer):

    pro_users =  userserializer(many = True,read_only = True)

    project_id = serializers.ReadOnlyField()
    class Meta:
        model = Project
        fields = "__all__"

