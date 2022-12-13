# Generated by Django 4.0.3 on 2022-03-12 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('floor', '0001_initial'),
        ('branch', '0001_initial'),
        ('unit', '0001_initial'),
        ('year', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('intime', models.DateTimeField()),
                ('outtime', models.DateTimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.branch')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floor.floor')),
                ('month', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='year.year')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.unit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
