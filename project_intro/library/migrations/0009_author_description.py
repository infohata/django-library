# Generated by Django 4.0.3 on 2022-03-07 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_bookinstance_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Description'),
        ),
    ]