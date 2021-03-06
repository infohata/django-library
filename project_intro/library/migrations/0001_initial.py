# Generated by Django 4.0.3 on 2022-03-02 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('last_name', models.CharField(db_index=True, max_length=100, verbose_name='Surname')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ex.: fiction, horror, history, hentai', max_length=200, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('summary', models.TextField(help_text='Short description of the book', max_length=1000, verbose_name='Summary')),
                ('isbn', models.CharField(help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN code</a>, max 13 symbols', max_length=13, verbose_name='ISBN')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author')),
                ('genre', models.ManyToManyField(help_text='Select genre(s) for this book', to='library.genre')),
            ],
        ),
    ]
