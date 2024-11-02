# Generated by Django 5.0.9 on 2024-11-01 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_archivespage'),
        ('postline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedArticlePage',
            fields=[
                ('articlepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.articlepage')),
                ('posted', models.BooleanField(default=False, help_text='Whether this article has been posted to Instagram')),
                ('instagram_link', models.URLField(blank=True, help_text='Link to the Instagram post', null=True)),
            ],
            options={
                'verbose_name': 'Extended Article Page',
                'verbose_name_plural': 'Extended Article Pages',
            },
            bases=('core.articlepage',),
        ),
        migrations.DeleteModel(
            name='PostlinePage',
        ),
    ]