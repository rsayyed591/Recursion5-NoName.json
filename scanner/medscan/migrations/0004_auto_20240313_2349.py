# Generated by Django 3.2.23 on 2024-03-13 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medscan', '0003_reportdetail_doctor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportdetail',
            name='report',
        ),
        migrations.RemoveField(
            model_name='reportdetail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='ReportDetail',
        ),
    ]