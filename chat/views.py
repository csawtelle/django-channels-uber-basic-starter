from django.shortcuts import render
from django.http import HttpResponse
from channels import Group
from django.contrib.auth.decorators import login_required
from .models import Message, Conversation, Contacts


@login_required
def ir(request):
  user = request.user
  conversations = Conversation.objects.filter(participants__contains=[user.username])
  chatdata = []
  for conversation in conversations:
    chatdata.append({
      "participants": (",".join(str(x) for x in conversation.participants)),
      "messages": Message.objects.filter(conversation=conversation)
    })

  return render(
    request, 
    "ir/ir.html", 
    {
      'username': user,
      'chatdata': chatdata
    }
  )

@login_required
def sendMessage(request):
  user = request.user
  if(request.method == "POST"):
    receiver = request.POST['consumer']
    print(receiver)
    receiver = receiver.split(',')
    if request.user.username not in receiver:
      receiver.append(user.username)
    receiver = list(set(receiver))
    print(receiver)
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
