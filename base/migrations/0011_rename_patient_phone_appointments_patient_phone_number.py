# Generated by Django 4.1.4 on 2023-01-04 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_rename_appointmentdate_appointments_appointment_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='patient_phone',
            new_name='patient_phone_number',
        ),
    ]
