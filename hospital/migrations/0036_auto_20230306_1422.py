# Generated by Django 3.0.5 on 2023-03-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0035_auto_20230306_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdischargedetails',
            name='testresults',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
