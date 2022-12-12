<<<<<<< HEAD
# Generated by Django 4.1.4 on 2022-12-10 13:34
=======
# Generated by Django 4.1.4 on 2022-12-10 12:32
>>>>>>> GuyEzra

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('age', models.PositiveIntegerField()),
                ('specialization', models.CharField(max_length=64)),
                ('educational_institution', models.CharField(max_length=64)),
                ('experience', models.PositiveIntegerField()),
                ('id_num', models.BigIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=64)),
                ('disease', models.CharField(max_length=64)),
                ('id_num', models.BigIntegerField()),
                ('smoking', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
    ]
