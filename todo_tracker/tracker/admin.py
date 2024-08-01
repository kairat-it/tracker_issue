from django.contrib import admin
from .models import Status, Type, Issue, Project

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Issue)
admin.site.register(Project)