# Generated by Django 4.2.4 on 2023-09-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_usersignupdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookinDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Package_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Package_Price', models.IntegerField(blank=True, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]