# Generated by Django 4.0.3 on 2022-03-12 10:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('nid', models.CharField(max_length=100)),
                ('member_type', models.CharField(max_length=100)),
                ('joining_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.branch')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
