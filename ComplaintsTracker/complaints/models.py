from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Complaint(models.Model):
    cpl_name = models.CharField('Complaint name', max_length=60)
    cpl_details = models.CharField('Complaint details', max_length=300)
    reporting_user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='reporting')
    cpl_creation_date = models.DateField('Reporting Date', auto_now_add=True)
    cpl_deadline = models.DateField('Deadline')
    cpl_closing_date = models.DateField('Closing Date', auto_now_add=True, null=True)
    closing_user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='closing')
    is_cpl_finished = models.BooleanField('Complaint is closed', default=False)

    def __str__(self):
        return self.cpl_name

    def is_approver_different_than_reporting_user(self):
        return self.reporting_user != self.closing_user


class Task(models.Model):
    complaint = models.ForeignKey(Complaint, blank=True, null=True, on_delete=models.CASCADE)
    tsk_name = models.CharField('Name', max_length=60)
    tsk_details = models.CharField('Details', max_length=200)
    assigned_user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='assigned')
    tsk_creation_date = models.DateField('Creation Date', auto_now_add=True)
    tsk_deadline = models.DateField('Deadline')
    tsk_closing_date = models.DateField('Closing Date', auto_now_add=True, null=True)
    is_tsk_finished = models.BooleanField('Task finished?', default=False)
    is_tsk_immediate = models.BooleanField('Task immediate?', default=False)

    def __str__(self):
        return self.tsk_name
