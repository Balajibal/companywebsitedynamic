# Generated by Django 3.1.1 on 2021-01-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='designation',
            field=models.CharField(max_length=200),
        ),
    ]
