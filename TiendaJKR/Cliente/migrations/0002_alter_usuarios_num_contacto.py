# Generated by Django 4.1.5 on 2023-01-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='num_contacto',
            field=models.IntegerField(),
        ),
    ]