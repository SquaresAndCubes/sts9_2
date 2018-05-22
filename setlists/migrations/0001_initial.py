# Generated by Django 2.0.5 on 2018-05-20 10:06

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.IntegerField()),
                ('segue', models.CharField(max_length=1, null=True)),
                ('notes', models.CharField(max_length=128, null=True)),
                ('guest', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_key', models.CharField(max_length=7)),
                ('date', models.DateField()),
            ],
            managers=[
                ('filters', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('cover', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='setlists.Venue'),
        ),
        migrations.AddField(
            model_name='set',
            name='songs',
            field=models.ManyToManyField(through='setlists.Performance', to='setlists.Song'),
        ),
        migrations.AddField(
            model_name='performance',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='setlists.Set'),
        ),
        migrations.AddField(
            model_name='performance',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='setlists.Show'),
        ),
        migrations.AddField(
            model_name='performance',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='setlists.Song'),
        ),
    ]
