# Generated by Django 5.1.3 on 2024-11-27 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0004_alter_bb_options_alter_bb_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['title', 'price'], 'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='bb',
            order_with_respect_to=None,
        ),
    ]
