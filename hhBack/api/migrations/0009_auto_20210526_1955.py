# Generated by Django 2.2 on 2021-05-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210526_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.CharField(default='21yyy-05-26', max_length=1000),
        ),
    ]
