# Generated by Django 4.1.1 on 2022-10-17 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='course',
        ),
        migrations.AlterModelTable(
            name='coursecategory',
            table='course_category',
        ),
    ]
