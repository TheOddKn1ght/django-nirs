# Generated by Django 4.2.7 on 2024-01-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_doctor_fio_remove_medicalstaff_fio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedure',
            name='description',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
