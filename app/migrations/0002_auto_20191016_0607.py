# Generated by Django 2.2.6 on 2019-10-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='essentialoil',
            name='abbr',
            field=models.CharField(default='a', max_length=10),
        ),
        migrations.AddField(
            model_name='essentialoil',
            name='family',
            field=models.CharField(default='a', max_length=100),
        ),
        migrations.AddField(
            model_name='essentialoil',
            name='sname',
            field=models.CharField(default='a', max_length=200),
        ),
    ]
