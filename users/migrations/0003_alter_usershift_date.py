# Generated by Django 4.1.5 on 2023-01-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usershift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershift',
            name='date',
            field=models.DateField(),
        ),
    ]