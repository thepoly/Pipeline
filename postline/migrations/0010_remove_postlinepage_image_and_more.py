# Generated by Django 5.0.9 on 2024-12-05 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postline', '0009_delete_postlineindexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlinepage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='postlinepage',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='postlinepage',
            name='posted',
        ),
    ]
