# Generated by Django 4.0.1 on 2022-01-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monster_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='id',
            field=models.IntegerField(primary_key=b'I01\n', serialize=False),
        ),
    ]
