# Generated by Django 3.1.7 on 2021-03-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210309_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
