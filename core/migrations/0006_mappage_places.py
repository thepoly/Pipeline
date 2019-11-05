# Generated by Django 2.2.1 on 2019-10-22 21:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_mappage'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappage',
            name='places',
            field=wagtail.core.fields.StreamField([('Locations', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.RichTextBlock(default='', required=True)), ('address', wagtail.core.blocks.RichTextBlock(default='', required=True)), ('description', wagtail.core.blocks.RichTextBlock(default='', required=True))]))], default=''),
            preserve_default=False,
        ),
    ]
