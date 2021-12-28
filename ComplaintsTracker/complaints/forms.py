from django import forms
from .models import *


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['cpl_name', 'cpl_details', 'cpl_deadline', 'closing_user']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['tsk_name', 'tsk_details', 'assigned_user', 'tsk_deadline', 'is_tsk_immediate']

