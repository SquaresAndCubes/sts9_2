# Generated by Django 2.0.5 on 2018-05-18 07:47

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='show',
            managers=[
                ('filter', django.db.models.manager.Manager()),
            ],
        ),
    ]