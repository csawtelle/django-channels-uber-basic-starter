from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import serializers


from chat import models as c


class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()
    class Meta:
        model = c.Conversation
        lookup_field = 'uid'
        fields = (
          'uid',
          'participants',
          'archived', 
        )

    def get_participants(self, obj):
         users = User.objects.filter(username__in=obj.participants)
         print(obj.participants)
         return users.values('id', 'username')


class ConversationsList(APIView):
  def get(self, request, format=None):
    conversations = c.Conversation.objects.all()
    serializer = ConversationSerializer(conversations, many=True)
    return Response(serializer.data)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = c.Message
        lookup_field = 'uid'
        fields = (
          'uid',
          'creator',
          'created', 
          'updated', 
          'archived', 
          'conversation',
          'content' 
        )

class MessagesList(APIView):
  def get(self, request, format=None):
    messages = c.Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
