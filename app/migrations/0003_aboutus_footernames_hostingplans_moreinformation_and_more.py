# Generated by Django 5.1.1 on 2024-10-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_hostingmain_hostingservice1_hostingservices_trusted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='FooterNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'Footer Names',
                'verbose_name_plural': 'Footer Names',
            },
        ),
        migrations.CreateModel(
            name='HostingPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(blank=True, max_length=200, null=True)),
                ('link_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Hosting Plans',
                'verbose_name_plural': 'Hosting Plans',
            },
        ),
        migrations.CreateModel(
            name='MoreInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link_url', models.CharField(blank=True, max_length=200, null=True)),
                ('link_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'More Information',
                'verbose_name_plural': 'More Information',
            },
        ),
        migrations.CreateModel(
            name='UsefulLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(blank=True, max_length=200, null=True)),
                ('link_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Useful Links',
                'verbose_name_plural': 'Useful Links',
            },
        ),
    ]
