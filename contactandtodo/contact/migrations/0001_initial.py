# Generated by Django 2.0.3 on 2018-03-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=200)),
                ('person_phone', models.CharField(max_length=200)),
                ('person_photo', models.CharField(max_length=200)),
            ],
        ),
    ]