# Generated by Django 4.0.1 on 2022-01-30 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='accepted_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
