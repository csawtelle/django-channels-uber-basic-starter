from django.contrib import admin
from .models import Message, Conversation, Contacts

class MessageAdmin(admin.ModelAdmin):
  list_filter = ('creator',)
  list_display = ('creator', 'conversation', 'content', 'created', 'updated')

class ConversationAdmin(admin.ModelAdmin):
  list_filter = ('participants',)
  list_display = ('participants', 'archived')

class ContactsAdmin(admin.ModelAdmin):
  list_filter = ('owner',)
  list_display = ('owner', 'contactList')

admin.site.register(Message, MessageAdmin)
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Contacts, ContactsAdmin)
