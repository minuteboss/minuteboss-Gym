# Generated by Django 4.0.5 on 2022-07-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_subplan_max_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subplan',
            name='price',
            field=models.IntegerField(),
        ),
    ]