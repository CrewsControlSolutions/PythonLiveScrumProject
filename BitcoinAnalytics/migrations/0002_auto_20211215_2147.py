# Generated by Django 2.2.5 on 2021-12-15 21:47

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('BitcoinAnalytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='competitor',
            managers=[
                ('Competition', django.db.models.manager.Manager()),
            ],
        ),
    ]
