# Generated by Django 4.0.5 on 2022-07-04 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0003_alter_mytext_board_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytext',
            name='categoty',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
