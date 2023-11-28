# Generated by Django 4.2.7 on 2023-11-28 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('room', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableDoctors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('available_time', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MedWorker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('anamnesis', models.TextField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medworker')),
            ],
        ),
        migrations.CreateModel(
            name='ProcedureJournal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('room', models.CharField(max_length=255)),
                ('anamnesis', models.TextField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medworker')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
        ),
        migrations.RemoveField(
            model_name='doctorcatalog',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='medicalstaff',
            name='user',
        ),
        migrations.RemoveField(
            model_name='medicalstaffcatalog',
            name='medical_staff',
        ),
        migrations.RemoveField(
            model_name='patientrecord',
            name='user',
        ),
        migrations.RemoveField(
            model_name='price',
            name='procedure',
        ),
        migrations.RemoveField(
            model_name='procedurecatalog',
            name='procedure',
        ),
        migrations.RemoveField(
            model_name='reception',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='reception',
            name='user',
        ),
        migrations.RemoveField(
            model_name='totalcost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='procedure',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='procedure',
            name='invoice_number',
        ),
        migrations.RemoveField(
            model_name='procedure',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='procedure',
            name='medical_staff',
        ),
        migrations.RemoveField(
            model_name='procedure',
            name='room_number',
        ),
        migrations.RemoveField(
            model_name='procedure',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='procedure',
            name='user',
        ),
        migrations.AddField(
            model_name='procedure',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procedure',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='procedure',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='DoctorCatalog',
        ),
        migrations.DeleteModel(
            name='MedicalStaff',
        ),
        migrations.DeleteModel(
            name='MedicalStaffCatalog',
        ),
        migrations.DeleteModel(
            name='PatientRecord',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.DeleteModel(
            name='ProcedureCatalog',
        ),
        migrations.DeleteModel(
            name='Reception',
        ),
        migrations.DeleteModel(
            name='TotalCost',
        ),
        migrations.AddField(
            model_name='procedurejournal',
            name='procedure_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.procedure'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medworker'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient'),
        ),
    ]
