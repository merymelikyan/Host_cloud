# Generated by Django 5.1.1 on 2024-10-11 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_aboutus_footernames_hostingplans_moreinformation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trustedmain',
            name='image',
        ),
    ]
