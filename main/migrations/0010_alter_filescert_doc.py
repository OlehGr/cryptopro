# Generated by Django 4.0.4 on 2022-05-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_certgost_remove_filescert_file_serv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filescert',
            name='doc',
            field=models.FileField(max_length=255, upload_to=''),
        ),
    ]
