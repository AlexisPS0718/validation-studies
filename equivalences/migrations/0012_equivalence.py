# Generated by Django 5.1 on 2024-08-31 02:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equivalences', '0011_delete_equivalence'),
        ('institutes', '0003_rename_syllabus_subject_career'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equivalence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('analysis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equivalences.analysis')),
                ('origin_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_subject', to='institutes.subject')),
                ('receiver_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_subject', to='institutes.subject')),
            ],
        ),
    ]
