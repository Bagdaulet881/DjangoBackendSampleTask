# Generated by Django 2.2 on 2021-05-26 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210526_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='company',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Vacancy',
        ),
    ]
