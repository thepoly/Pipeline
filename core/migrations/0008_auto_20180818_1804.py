# Generated by Django 2.0.8 on 2018-08-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0007_staffpage_email_address")]

    operations = [
        migrations.AlterField(
            model_name="staffpage",
            name="first_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="staffpage",
            name="last_name",
            field=models.CharField(max_length=100),
        ),
    ]