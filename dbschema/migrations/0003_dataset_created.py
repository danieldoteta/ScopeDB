# Generated by Django 3.2.6 on 2021-08-31 16:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dbschema', '0002_rename_datasets_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
