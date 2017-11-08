from channels import Group

def ws_connect(message):
    Group("sensor").add(message.reply_channel)
    message.reply_channel.send({
      "text": "Connected",
    })

def ws_message(message):
    print("Received!!" + message['text'])

def ws_disconnect(message):
  print("Someone left us...")
  Group("sensor").discard(message.reply_channel)
