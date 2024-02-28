"""
Tests for models.
"""

from django.test import TestCase

from core import models
from datetime import datetime

def create_vessel():
    return models.Vessel.objects.create(
        vessel_name="RSS Tester"
    )

def create_vessel_schedule():
    return models.VesselSchedule.objects.create(
        vessel = create_vessel(),
        voyage_number = "1243362314",
        arrival_date = datetime.now()
    )

def create_bill_of_lading():
    return models.BillOfLading.objects.create(
        voyage = create_vessel_schedule(),
        bol_number = "12451521",
        contact_name = "Jane Doe",
        contact_number = "8311231155",
        contact_email = "testTwo@tester.com",
        release_status = "C"
    )

class ModelTests(TestCase):

    def test_create_vessel(self):
        """Test Creating a Vessel is Successful"""
        vessel = models.Vessel.objects.create(
            vessel_name="RSS Tester"
        )

        self.assertEqual(str(vessel), vessel.vessel_name)

    def test_create_vessel_schedule(self):
        """Test Creating a Vessel Schedule is Successful"""
        vessel_schedule = models.VesselSchedule.objects.create(
            vessel = create_vessel(),
            voyage_number = "1244412421",
            arrival_date = datetime.now()
        )

        self.assertEqual(str(vessel_schedule), str(vessel_schedule.vessel.vessel_name)+"-"+str(vessel_schedule.voyage_number))

    def test_BillOfLading(self):
        """Test Creating a Bill of Lading is Successful"""
        billOfLading = models.BillOfLading.objects.create(
            voyage = create_vessel_schedule(),
            bol_number = "1245521",
            contact_name = "John Doe",
            contact_number = "8311231123",
            contact_email = "test@tester.com",
            release_status = "S"
        )

        self.assertEqual(str(billOfLading), str(billOfLading.bol_number))

    def test_container(self):
        """Test Creating a Container is Successful"""
        container = models.Container.objects.create(
            bol = create_bill_of_lading(),
            container_number = "1123141411"
        ) 

        self.assertEqual(str(container), str(container.container_number))