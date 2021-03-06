# Generated by Django 3.1.7 on 2021-03-09 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='New York', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
