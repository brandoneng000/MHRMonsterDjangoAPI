# Generated by Django 4.0.1 on 2022-01-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.IntegerField(max_length=3, primary_key=b'I01\n', serialize=False)),
                ('monster_name', models.CharField(max_length=50)),
            ],
        ),
    ]
