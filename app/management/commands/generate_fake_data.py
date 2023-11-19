from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from datetime import timedelta
from app.models import MedicalStaff, Doctor, Reception, Procedure, Price, TotalCost, PatientRecord, DoctorCatalog, ProcedureCatalog, MedicalStaffCatalog
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Generating fake data...'))

        self.generate_fake_data()

        self.stdout.write(self.style.SUCCESS('Fake data generated successfully!'))

    def create_fake_user(self):
        username = f"{fake.user_name()}_{fake.random_number(digits=3)}"  # Append a unique identifier
        email = fake.email()
        password = fake.password()

        user = User.objects.create_user(username=username, email=email, password=password)
        return user


    def create_fake_medical_staff(self):
        user = self.create_fake_user()
        education = fake.word()

        return MedicalStaff.objects.create(user=user, education=education)

    def create_fake_doctor(self):
        medical_staff = self.create_fake_medical_staff()

        return Doctor.objects.create(medical_staff=medical_staff)

    def create_fake_reception(self):
        start_time = fake.date_time_this_decade()
        end_time = start_time + timedelta(hours=random.randint(1, 3))
        doctor = self.create_fake_doctor()
        user = self.create_fake_user()

        return Reception.objects.create(start_time=start_time, end_time=end_time, doctor=doctor, user=user)

    def create_fake_procedure(self):
        start_time = fake.date_time_this_decade()
        end_time = start_time + timedelta(minutes=random.randint(30, 120))
        room_number = random.randint(1, 10)
        invoice_number = random.randint(1000, 9999) if random.choice([True, False]) else None
        medical_staff = self.create_fake_medical_staff()
        user = self.create_fake_user()
        is_paid = random.choice([True, False])

        return Procedure.objects.create(start_time=start_time, end_time=end_time, room_number=room_number,
                                        invoice_number=invoice_number, medical_staff=medical_staff, user=user, is_paid=is_paid)

    def create_fake_price(self):
        amount = round(random.uniform(50, 500), 2)
        procedure = self.create_fake_procedure()

        return Price.objects.create(amount=amount, procedure=procedure)

    def create_fake_total_cost(self):
        amount = round(random.uniform(100, 1000), 2)
        user = self.create_fake_user()

        return TotalCost.objects.create(amount=amount, user=user)

    def create_fake_patient_record(self):
        user = self.create_fake_user()
        description = fake.text()

        return PatientRecord.objects.create(user=user, description=description)

    def create_fake_doctor_catalog(self):
        doctor = self.create_fake_doctor()

        return DoctorCatalog.objects.create(doctor=doctor)

    def create_fake_procedure_catalog(self):
        procedure = self.create_fake_procedure()

        return ProcedureCatalog.objects.create(procedure=procedure)

    def create_fake_medical_staff_catalog(self):
        medical_staff = self.create_fake_medical_staff()

        return MedicalStaffCatalog.objects.create(medical_staff=medical_staff)

    def generate_fake_data(self, num_entries=10):
        for _ in range(num_entries):
            self.create_fake_reception()
            self.create_fake_price()
            self.create_fake_total_cost()
            self.create_fake_patient_record()
            self.create_fake_doctor_catalog()
            self.create_fake_procedure_catalog()
            self.create_fake_medical_staff_catalog()

if __name__ == "__main__":
    command = Command()
    command.handle()
