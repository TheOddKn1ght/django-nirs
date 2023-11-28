import os
from django.core.management.base import BaseCommand
from faker import Faker
from app.models import MedWorker, Procedure, Appointment, ProcedureJournal, AvailableDoctors, Patient
from django.utils import timezone

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for testing purposes'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data generation...'))

        num_medworkers = 10
        num_procedures = 5
        num_patients = 20
        num_appointments = 30
        num_procedure_journal_entries = 25
        num_available_doctors = 15

        self.create_fake_medworkers(num_medworkers)
        self.create_fake_procedures(num_procedures)

        doctors = MedWorker.objects.filter(position='Doctor')
        self.create_fake_patients(num_patients, doctors)
        patients = Patient.objects.all()

        self.create_fake_appointments(num_appointments, patients, doctors)
        self.create_fake_procedure_journal_entries(num_procedure_journal_entries, patients, doctors, Procedure.objects.all())
        self.create_fake_available_doctors(num_available_doctors)

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully!'))

    def create_fake_medworkers(self, num_records):
        for _ in range(num_records):
            MedWorker.objects.create(
                full_name=fake.name(),
                phone=fake.phone_number(),
                department=fake.job(),
                position=fake.random_element(elements=('Doctor', 'Nurse', 'Technician'))
            )

    def create_fake_procedures(self, num_records):
        for _ in range(num_records):
            Procedure.objects.create(
                name=fake.word(),
                cost=fake.pydecimal(left_digits=3, right_digits=2, positive=True)
            )

    def create_fake_patients(self, num_records, doctors):
        for _ in range(num_records):
            doctor = fake.random_element(doctors)
            Patient.objects.create(
                full_name=fake.name(),
                phone=fake.phone_number(),
                email=fake.email(),
                doctor_id=doctor,
                anamnesis=fake.text()
            )

    def create_fake_appointments(self, num_records, patients, doctors):
        for _ in range(num_records):
            patient = fake.random_element(patients)
            doctor = fake.random_element(doctors)
            Appointment.objects.create(
                date_time=fake.future_datetime(),
                email=patient.email,
                patient_id=patient,
                doctor_id=doctor,
                room=fake.random_int(min=1, max=10)
            )

    def create_fake_procedure_journal_entries(self, num_records, patients, doctors, procedures):
        for _ in range(num_records):
            patient = fake.random_element(patients)
            doctor = fake.random_element(doctors)
            procedure = fake.random_element(procedures)
            ProcedureJournal.objects.create(
                procedure_id=procedure,
                patient_id=patient,
                doctor_id=doctor,
                date=fake.past_date(),
                room=fake.random_int(min=1, max=10),
                anamnesis=fake.text()
            )

    def create_fake_available_doctors(self, num_records):
        for _ in range(num_records):
            AvailableDoctors.objects.create(
                full_name=fake.name(),
                department=fake.random_element(elements=('Cardiology', 'Orthopedics', 'Dermatology')),
                available_time=fake.random_element(elements=('Morning', 'Afternoon', 'Evening'))
            )
