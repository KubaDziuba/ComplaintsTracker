from django.test import TestCase
from django.contrib.auth.models import User

from .models import Complaint


class ComplaintModelTests(TestCase):

    def test_is_approver_different_than_reporting_user(self):
        """
        test if approver check works
        """
        test_user = User.objects.create_user('Mark', 'mark@test.com', 'pass')
        complaint = Complaint(reporting_user=test_user, closing_user=test_user)
        self.assertIs(complaint.is_approver_different_than_reporting_user(), False)
