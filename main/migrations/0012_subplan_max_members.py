# Generated by Django 4.0.5 on 2022-07-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_subplanfeatures_subplan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='max_members',
            field=models.IntegerField(null=True),
        ),
    ]
