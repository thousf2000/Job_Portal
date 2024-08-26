# Generated by Django 5.0.7 on 2024-08-25 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='featured_images/')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('job_title', models.CharField(max_length=255)),
                ('job_description', models.TextField()),
                ('job_type', models.CharField(choices=[('freelance', 'Freelance'), ('contract', 'Contract'), ('internship', 'Internship')], max_length=50)),
                ('tag', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('apply_type', models.CharField(choices=[('online', 'Online'), ('inperson', 'Inperson')], max_length=50)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('apply_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('salary_type', models.CharField(choices=[('cheque', 'Cheque'), ('cash', 'Cash')], max_length=50)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('max_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('experience', models.CharField(choices=[('year1', '0-1 year'), ('year2', '2-3 years')], max_length=50)),
                ('career_level', models.CharField(choices=[('entry', 'Entry-Level'), ('senior', 'Senior-Level')], max_length=50)),
                ('intro_video_url', models.URLField(blank=True, null=True)),
                ('application_deadline', models.DateField()),
                ('friendly_address', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.qualification')),
            ],
        ),
    ]
