# Generated by Django 5.1.1 on 2024-10-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_trustedmain_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Cloud Main',
                'verbose_name_plural': 'Cloud Main',
            },
        ),
        migrations.CreateModel(
            name='CloudPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('duration', models.CharField(max_length=255)),
                ('space', models.CharField(max_length=255)),
                ('transfer', models.CharField(max_length=255)),
                ('panel', models.CharField(max_length=255)),
                ('support', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('upgrading', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Cloud Plan',
                'verbose_name_plural': 'Cloud Plans',
            },
        ),
        migrations.CreateModel(
            name='FeaturesBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='features_blocks')),
            ],
            options={
                'verbose_name': 'Features Blocks',
                'verbose_name_plural': 'Features Blocks',
            },
        ),
        migrations.CreateModel(
            name='FeaturesMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Feutares Main',
                'verbose_name_plural': 'Feutares Main',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Testimonials',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='TestimonialsBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('icon_class', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Testimonials Blocks',
                'verbose_name_plural': 'Testimonials Blocks',
            },
        ),
        migrations.AlterField(
            model_name='trusted',
            name='image',
            field=models.ImageField(upload_to='trusted'),
        ),
    ]
