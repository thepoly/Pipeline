# Generated by Django 2.0.7 on 2018-07-17 16:12

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articlesindex'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='subdeck',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='summary',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Displayed on the home page or other places to provide a taste of what the article is about.', null=True),
        ),
    ]