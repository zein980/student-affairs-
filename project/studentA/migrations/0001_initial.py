# Generated by Django 4.0.4 on 2022-05-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('idst', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=60)),
                ('level', models.IntegerField()),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
