# Generated by Django 2.0 on 2017-12-07 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171206_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='name',
        ),
    ]