# Generated by Django 5.0.6 on 2024-06-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('preffered_subject', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
