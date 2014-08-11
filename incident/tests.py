from django.db import IntegrityError
from django.test import TestCase
from structure.models import Contract, Organization, Team, User
from incident.models import Issue

class IssueTest(TestCase):

    def setUp(self):
        """
        Initialize test environment.
        """
        self.organization_t = Organization.objects.create(name="Test_Organization")
        self.team_t = Team.objects.create(name="Test_Team",
                                          organization=self.organization_t)
        self.user_t = User.objects.create(name="Test_User")
        self.team_t.users.add(self.user_t)
        self.contract_t = Contract.objects.create(name="Test_Contract")

    def test_issue_create_ko(self):
        """
        Test empty object creation.
        """
        self.assertRaises(IntegrityError, Issue.objects.create)

    def test_issue_create_ok(self):
        """
        Test correct Issue creation.
        """
        issue_t = Issue.objects.create(title="LIIT",
                                        description="Do you like it ?",
                                        contract=self.contract_t,
                                        assigned_team=self.team_t,
                                        assigned_user=self.user_t)
        self.assertEqual(issue_t.title,'LIIT')
        self.assertEqual(issue_t.description,'Do you like it ?')
        self.assertEqual(issue_t.assigned_user.name, "Test_User")
        self.assertEqual(issue_t.assigned_team.name, "Test_Team")
        self.assertIsNotNone(issue_t.created_at)

