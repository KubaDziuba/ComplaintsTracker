from django.contrib import admin

# Register your models here.

from .models import Complaint, Task

admin.site.register(Complaint)
admin.site.register(Task)
