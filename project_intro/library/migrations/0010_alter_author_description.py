# Generated by Django 4.0.3 on 2022-03-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_author_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, default='', max_length=200, verbose_name='Description'),
        ),
    ]