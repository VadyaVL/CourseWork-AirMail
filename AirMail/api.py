from models import *
from serializers import *

from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
import mypermissions
from rest_framework import status
from rest_framework import permissions

class DialogueList(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, format=None):
        dialogue = Dialogue.objects.all()
        serializer = DialogueSerializer(dialogue, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DialogueSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DialogueDetail(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, mypermissions.IsOwnerOrReadOnly)

    def get_object(selfself, pk):
        try:
            return Dialogue.objects.get(pk=pk)
        except Dialogue.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dialogue = self.get_object(pk)
        serialized_dialogue = DialogueSerializer(dialogue, context={'request': request})
        return Response(serialized_dialogue.data)

    def put(self, request, pk, format=None):
        dialogue = self.get_object(pk)
        serializer = DialogueSerializer(dialogue, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dialogue = self.get_object(pk)
        dialogue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, mypermissions.IsOwnerOrReadOnly)

    def get_object(selfself, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        info = self.get_object(pk)
        serialized = UserSerializer(info, context={'request': request})
        return Response(serialized.data)

    def put(self, request, pk, format=None):
        info = self.get_object(pk)
        serializer = UserSerializer(info, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Informaion

class InformationList(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        info = Information.objects.all()
        serializer = InformationSerializer(info, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InformationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InformationDetail(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, mypermissions.IsOwnerOrReadOnly)

    def get_object(selfself, pk):
        try:
            return Information.objects.get(pk=pk)
        except Information.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        info = self.get_object(pk)
        serialized = InformationSerializer(info, context={'request': request})
        return Response(serialized.data)

    def put(self, request, pk, format=None):
        info = self.get_object(pk)
        serializer = InformationSerializer(info, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        info = self.get_object(pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)