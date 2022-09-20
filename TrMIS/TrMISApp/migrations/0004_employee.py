# Generated by Django 4.1.1 on 2022-09-20 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrMISApp', '0003_organizaion_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=200, verbose_name='employee name')),
                ('employee_address', models.CharField(max_length=200, verbose_name='employee address')),
                ('age', models.IntegerField()),
                ('organization_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrMISApp.organizaion')),
            ],
        ),
    ]
