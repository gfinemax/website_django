# Generated by Django 4.0.1 on 2022-01-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]