# Generated by Django 3.2 on 2021-04-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_profile_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unique_code',
            field=models.CharField(default='NvZ4ndBdm', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]