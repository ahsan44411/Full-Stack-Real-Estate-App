# Generated by Django 3.1.7 on 2021-03-09 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='top_sellet',
            new_name='top_seller',
        ),
    ]
