# Generated by Django 3.1.4 on 2021-01-07 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('publication_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255, verbose_name='Изображение')),
                ('label', models.BooleanField(default=False, verbose_name='')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComicsReader.comic')),
            ],
        ),
    ]
