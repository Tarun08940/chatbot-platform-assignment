from django.contrib import admin
from .models import Project, Prompt, ChatMessage

admin.site.register(Project)
admin.site.register(Prompt)
admin.site.register(ChatMessage)
