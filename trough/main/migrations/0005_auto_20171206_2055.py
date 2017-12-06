# Generated by Django 2.0 on 2017-12-06 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171206_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='dish',
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredients',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Ingredient'),
        ),
    ]
