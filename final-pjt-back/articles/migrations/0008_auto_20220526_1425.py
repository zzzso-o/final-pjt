# Generated by Django 3.1.3 on 2022-05-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20220526_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='article_comment_created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='article_comment_updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
