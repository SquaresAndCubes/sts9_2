# Generated by Django 2.0.5 on 2018-06-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='segue',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='country',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='venue',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
