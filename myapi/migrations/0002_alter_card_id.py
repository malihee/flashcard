# Generated by Django 4.0.2 on 2022-02-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]