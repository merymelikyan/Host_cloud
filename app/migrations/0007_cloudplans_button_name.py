# Generated by Django 5.1.1 on 2024-10-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_cloudplans_price_alter_featuresblocks_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloudplans',
            name='button_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]