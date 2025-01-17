# Generated by Django 5.1.3 on 2024-12-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_alter_bb_options_alter_bb_order_with_respect_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
