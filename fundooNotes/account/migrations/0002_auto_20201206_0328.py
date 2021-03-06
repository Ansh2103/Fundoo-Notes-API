# Generated by Django 3.1.4 on 2020-12-06 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetail',
            name='email',
            field=models.EmailField(max_length=25),
        ),
        migrations.AlterField(
            model_name='accountdetail',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='accountdetail',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='accountdetail',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
