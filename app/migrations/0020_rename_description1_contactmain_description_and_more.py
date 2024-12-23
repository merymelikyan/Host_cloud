# Generated by Django 5.1.1 on 2024-10-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_tag_contactmain_description1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmain',
            old_name='description1',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='contactmain',
            old_name='description2',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='contactmain',
            old_name='tag1',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='html_class',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='title',
        ),
        migrations.RemoveField(
            model_name='contactmain',
            name='tag2',
        ),
        migrations.RemoveField(
            model_name='contactmain',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='contactmain',
            name='title2',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='html_class1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='html_class2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='html_name1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='html_name2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='title1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='title2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
