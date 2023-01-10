# Generated by Django 4.1.4 on 2023-01-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dte', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField()),
                ('address', models.CharField(max_length=64)),
                ('symptoms', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-dte'],
            },
        ),
    ]