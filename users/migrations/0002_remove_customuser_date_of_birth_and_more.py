# Generated by Django 4.1.5 on 2023-01-02 18:46

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='surname_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(default='Main', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='position',
            field=models.CharField(default='Manager', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='lankas', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(auto_now_add=True, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=60, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateField(auto_now=True, default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=False,
        ),
    ]