# Generated by Django 4.1.10 on 2023-09-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_alter_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=250, verbose_name='название'),
        ),
    ]
