# Generated by Django 3.2 on 2021-04-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='contact',
            field=models.CharField(default='', max_length=10),
        ),
    ]