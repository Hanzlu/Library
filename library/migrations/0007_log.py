# Generated by Django 3.2.23 on 2023-12-31 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_book_returntime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0)),
                ('request', models.CharField(max_length=100)),
                ('borrowed', models.IntegerField(default=0)),
                ('tokens', models.IntegerField(default=0)),
            ],
        ),
    ]
