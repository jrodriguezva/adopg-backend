from django.test import TestCase
from phonenumbers import PhoneNumber
import pytest

from applications.organization.models import *
from model_bakery import baker

@pytest.mark.django_db
class OrganizationTestCase(TestCase):
    def setUp(self):
        self.organization = baker.make('organization.Organization', phone="+34658899664")

    def test_organization(self):
        assert isinstance(self.organization, Organization)
        assert isinstance(self.organization.phone, PhoneNumber)
        assert self.organization.phone == "+34658899664"
        assert self.organization.phone.country_code == 34

    def test_organization_has_hour(self):
        self.assertIsNotNone(self.organization.hours)

    def test_organization_has_address(self):
        self.assertIsNotNone(self.organization.address)

    def test_organization_has_social_media(self):
        self.assertIsNotNone(self.organization.social_media)
