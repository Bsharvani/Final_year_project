# Generated by Django 2.0.2 on 2018-04-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0019_auto_20180406_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
