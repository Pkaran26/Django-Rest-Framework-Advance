# Generated by Django 2.1.4 on 2019-04-13 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190413_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='reach',
        ),
        migrations.AddField(
            model_name='reached',
            name='article',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
            preserve_default=False,
        ),
    ]
