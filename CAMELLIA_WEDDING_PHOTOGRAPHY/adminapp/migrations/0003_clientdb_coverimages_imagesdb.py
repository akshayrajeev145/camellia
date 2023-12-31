# Generated by Django 4.2.4 on 2023-08-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_rename_photographycategory_categorydb'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientName', models.CharField(blank=True, max_length=100, null=True)),
                ('ClientEventCategory', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoverImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CoverCategoryName', models.CharField(blank=True, max_length=100, null=True)),
                ('CoverCategoryIamges', models.ImageField(blank=True, null=True, upload_to='Cover-Category_Image')),
            ],
        ),
        migrations.CreateModel(
            name='ImagesDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IMGCategoryName', models.CharField(blank=True, max_length=100, null=True)),
                ('IMGClientName', models.CharField(blank=True, max_length=100, null=True)),
                ('Images', models.ImageField(blank=True, null=True, upload_to='Event-Images')),
            ],
        ),
    ]
