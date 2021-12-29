from django import forms
from .models import *
from django.contrib.auth.models import User


class ComplaintForm(forms.ModelForm):
    closing_user = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Manager'), empty_label='')

    class Meta:
        model = Complaint
        fields = ['cpl_name', 'cpl_details', 'cpl_deadline']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['tsk_name', 'tsk_details', 'assigned_user', 'tsk_deadline', 'is_tsk_immediate']

