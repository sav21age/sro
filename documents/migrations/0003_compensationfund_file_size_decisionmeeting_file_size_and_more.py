# Generated by Django 4.1.10 on 2023-09-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_remove_compensationfund_file_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compensationfund',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='decisionmeeting',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='federallaw',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='foundingdocument',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='localregulation',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='regulatorylegal',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='reporting',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='soutresult',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
        migrations.AddField(
            model_name='technicalregulation',
            name='file_size',
            field=models.PositiveBigIntegerField(default=0, verbose_name='размер файла в байтах'),
        ),
    ]