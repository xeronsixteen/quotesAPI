# Generated by Django 4.1.1 on 2022-09-27 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'permissions': [('moderator', 'модератор')], 'verbose_name': 'Quote', 'verbose_name_plural': 'Quotes'},
        ),
    ]