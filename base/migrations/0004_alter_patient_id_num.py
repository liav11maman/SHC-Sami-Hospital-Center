# Generated by Django 4.1.4 on 2022-12-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_doctor_id_num_alter_patient_id_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id_num',
            field=models.BigIntegerField(),
        ),
    ]
