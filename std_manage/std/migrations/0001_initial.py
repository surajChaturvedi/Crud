# Generated by Django 4.2.2 on 2023-06-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=100)),
                ('uemail', models.CharField(max_length=100)),
                ('ucontact', models.CharField(max_length=100)),
            ],
        ),
    ]
