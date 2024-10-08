# Generated by Django 5.1 on 2024-09-03 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equivalences', '0013_alter_docanalysis_created_at'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docanalysis',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='analysis', serialize=False, to='students.student'),
        ),
    ]
