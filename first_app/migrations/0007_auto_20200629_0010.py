# Generated by Django 2.2.6 on 2020-06-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_post_postdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='PostDate',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
    ]
