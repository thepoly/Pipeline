# Generated by Django 2.2.9 on 2020-02-15 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("core", "0033_office_description")]

    operations = [migrations.RemoveField(model_name="office", name="election_in")]
