# Generated by Django 5.0.1 on 2024-02-07 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0005_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]
