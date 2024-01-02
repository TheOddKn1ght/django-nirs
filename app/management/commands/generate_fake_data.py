import random
from faker import Faker
from django.core.management.base import BaseCommand
from app.models import Procedure, Doctor, MedicalStaff, Patient, ProcedureLog, Appointment

fake = Faker()

class Command(BaseCommand):
    help = 'Populate all models with fake data'

    def add_arguments(self, parser):
        parser.add_argument('num_entries', type=int, default=10, help='Number of fake entries to generate for each model')

    def handle(self, *args, **options):
        num_entries = options['num_entries']
        self.generate_fake_procedures(num_entries)
        self.generate_fake_doctors(num_entries)
        self.generate_fake_medical_staff(num_entries)
        self.generate_fake_patients(num_entries)
        self.generate_fake_procedure_logs(num_entries)
        self.generate_fake_appointments(num_entries)

        self.stdout.write(self.style.SUCCESS(f'Fake data for {num_entries} entries generated successfully for all models.'))

    def generate_fake_procedures(self, num_entries):
        for _ in range(num_entries):
            Procedure.objects.create(
                name=fake.word(),
                cost=random.uniform(50, 200),
                description=fake.text()
            )

    def generate_fake_doctors(self, num_entries):
        for _ in range(num_entries):
            Doctor.objects.create(
                first_name=fake.first_name(),
                second_name=fake.first_name(),
                last_name=fake.last_name(),
                department=fake.word(),
                time=fake.date_time_this_year()
            )

    def generate_fake_medical_staff(self, num_entries):
        for _ in range(num_entries):
            MedicalStaff.objects.create(
                first_name=fake.first_name(),
                second_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                department=fake.word(),
                position=fake.word()
            )

    def generate_fake_patients(self, num_entries):
        for _ in range(num_entries):
            Patient.objects.create(
                first_name=fake.first_name(),
                second_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email(),
                doctor_id=random.randint(1, num_entries),
                medical_history=fake.text()
            )

    def generate_fake_procedure_logs(self, num_entries):
        for _ in range(num_entries):
            ProcedureLog.objects.create(
                patient_id=random.randint(1, num_entries),
                doctor_id=random.randint(1, num_entries),
                date=fake.date_time_this_year(),
                room=random.randint(1, num_entries),
                medical_history=fake.text()
            )

    def generate_fake_appointments(self, num_entries):
        for _ in range(num_entries):
            Appointment.objects.create(
                date_time=fake.date_time_this_year(),
                email=fake.email(),
                patient_id=random.randint(1, num_entries),
                doctor_id=random.randint(1, num_entries),
                room=random.randint(1, num_entries)
            )
