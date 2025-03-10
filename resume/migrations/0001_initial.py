# Generated by Django 5.1.5 on 2025-03-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=60)),
                ('email', models.EmailField(max_length=80)),
                ('password', models.TextField(max_length=80)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload/')),
                ('skills', models.TextField(max_length=200)),
                ('qualifications', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=300)),
            ],
        ),
    ]
