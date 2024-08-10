# Generated by Django 5.0.7 on 2024-08-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['slug']},
        ),
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.URLField(),
        ),
    ]
