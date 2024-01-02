import random
from faker import Faker
from django.core.management.base import BaseCommand
from app.models import MedicalStaff, Procedure, Patient, ProcedureLog, Appointment

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        self.generate_fake_medical_staff()
        self.generate_fake_procedures()
        self.generate_fake_patients()
        self.generate_fake_procedure_logs()
        self.generate_fake_appointments()
        self.stdout.write(self.style.SUCCESS('Fake data generated successfully.'))

    def generate_fake_medical_staff(self):
        positions = ['Doctor', 'Nurse', 'Receptionist']
        for _ in range(5):
            MedicalStaff.objects.create(
                fio=fake.name(),
                phone=fake.phone_number(),
                department=fake.word(),
                position=random.choice(positions)
            )

    def generate_fake_procedures(self):
        for _ in range(5):
            Procedure.objects.create(
                name=fake.word(),
                cost=random.uniform(50, 200)
            )

    def generate_fake_patients(self):
        for _ in range(10):
            Patient.objects.create(
                fio=fake.name(),
                phone=fake.phone_number(),
                email=fake.email(),
                doctor_id=random.randint(1, 5),
                medical_history=fake.text()
            )

    def generate_fake_procedure_logs(self):
        for _ in range(20):
            ProcedureLog.objects.create(
                patient_id=random.randint(1, 10),
                doctor_id=random.randint(1, 5),
                date=fake.date_time_this_year(),
                room=random.randint(1, 5),
                medical_history=fake.text()
            )

    def generate_fake_appointments(self):
        for _ in range(10):
            Appointment.objects.create(
                date_time=fake.date_time_this_year(),
                email=fake.email(),
                patient_id=random.randint(1, 10),
                doctor_id=random.randint(1, 5),
                room=random.randint(1, 5)
            )
