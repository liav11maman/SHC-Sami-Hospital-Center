# Generated by Django 4.1.4 on 2023-01-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_blooddon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddon',
            name='blood_type',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
