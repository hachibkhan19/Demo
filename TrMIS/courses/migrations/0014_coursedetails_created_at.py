# Generated by Django 4.1.1 on 2022-10-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_coursedetails_start_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='created_at',
            field=models.DateField(default='2022-12-13'),
        ),
    ]
