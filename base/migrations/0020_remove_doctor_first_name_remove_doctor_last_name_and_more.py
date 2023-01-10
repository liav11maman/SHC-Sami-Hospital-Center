# Generated by Django 4.1.4 on 2023-01-08 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_appointment_patient_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='full_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='password',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='username',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='educational_institution',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id_num',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
