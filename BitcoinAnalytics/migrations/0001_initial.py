# Generated by Django 2.2.5 on 2021-12-15 18:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('linkedIn', models.CharField(max_length=100)),
            ],
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
    ]
