# Generated by Django 3.2.23 on 2024-03-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medscan', '0002_rename_pcv_reportdetail_mch'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportdetail',
            name='doctor_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]