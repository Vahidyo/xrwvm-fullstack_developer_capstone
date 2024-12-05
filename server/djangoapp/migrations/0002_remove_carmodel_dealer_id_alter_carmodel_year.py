# Generated by Django 5.1.3 on 2024-12-04 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='dealer_id',
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(default=2023, help_text='The year this car model was manufactured.'),
        ),
    ]