# Generated by Django 3.1.7 on 2021-03-13 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210313_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title_en',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
