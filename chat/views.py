from django.shortcuts import render
from django.http import HttpResponse
from channels import Group
from django.contrib.auth.decorators import login_required
from .models import Message, Conversation, Contacts


@login_required
def ir(request):
  user = request.user
  return render(
    request, 
    "ir/ir.html", 
    {
      'username': user,
      'recipients': ['user1', 'user2', 'user3'],
    }
  )

@login_required
def sendMessage(request):
  user = request.user
  if(request.method == "POST"):
    receiver = request.POST.getlist('consumer[]')
    receiver.append(user.username)
    message = request.POST['message']
    conversation, created = Conversation.objects.get_or_create(participants=receiver)
    Message.objects.create(creator=user, content=message, conversation=conversation)
    Group("sensor").send({'text': message})
    return HttpResponse('200')

@login_required
def receiveMessage(request):
  #user = request.user
  Group("sensor").send({"text": "Pushed receive"})
  return HttpResponse('200')
