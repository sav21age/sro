# Generated by Django 4.1.10 on 2023-09-06 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compensationfundpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='decisionmeetingpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='federallawpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='inspectionpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='joinuspage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='localregulationpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='memberexcludedpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='memberpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='prioritydirectionpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='regulatorylegalpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='reportingpage',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='technicalregulationpage',
            name='is_visible',
        ),
    ]