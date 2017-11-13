from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import uuid

class Conversation(models.Model):
  uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  participants = ArrayField(
    ArrayField(
      models.TextField(blank=False)
    )
  )
  archived = models.BooleanField(default=False)

  def __str__(self):
    string = str(self.participants)
    return string

class Message(models.Model):
  uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  creator = models.ForeignKey(User)
  content = models.TextField(default='Test Message', blank=False)
  created = models.DateTimeField(auto_now_add=True, editable=False)
  updated = models.DateTimeField(auto_now=True)
  archived = models.BooleanField(default=False)
  conversation = models.ForeignKey(Conversation, null=True)

  def __str__(self):
    string = str(self.content)
    return string

class Contacts(models.Model):
  uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  owner = models.ForeignKey(User)
  contactList = ArrayField(
    ArrayField(
      models.TextField(blank=False)
    )
  )
