# Generated by Django 3.2 on 2021-04-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_user_code_profile_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='unique_code',
            field=models.CharField(default='EAbD28miDM', editable=False, max_length=10),
        ),
    ]
