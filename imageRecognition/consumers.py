from channels import Group

def ws_connect(message):
  Group("sensor").add(message.reply_channel)
  Group("sensor").send({"accept": True})
  print("Websocket user connected.")

def ws_message(message):
  print("Received!!" + message['text'])

def ws_disconnect(message):
  print("Websocket user disconnected.")
  Group("sensor").discard(message.reply_channel)
