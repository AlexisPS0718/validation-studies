# Generated by Django 5.1 on 2024-08-15 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('is_engineering', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('republic_state', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('career', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='institutes.career')),
                ('key', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('final_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='career',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institutes.institute'),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('syllabus', models.ManyToManyField(to='institutes.career')),
            ],
        ),
    ]
