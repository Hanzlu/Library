# Generated by Django 3.2.23 on 2023-12-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_returnid'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='returnTime',
            field=models.IntegerField(default=0),
        ),
    ]
