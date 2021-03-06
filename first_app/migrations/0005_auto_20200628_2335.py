# Generated by Django 2.2.6 on 2020-06-28 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_userprofileinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myPost', models.TextField(max_length=1000)),
                ('post_title', models.CharField(default='Title Not Available', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.AddField(
            model_name='topic',
            name='top_desc',
            field=models.TextField(default='Description not available', max_length=300),
        ),
        migrations.AddField(
            model_name='post',
            name='myTopic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Topic'),
        ),
    ]
