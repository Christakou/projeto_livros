# Generated by Django 3.1.7 on 2021-03-14 19:42

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210314_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1800, 1800], upload_to=''),
        ),
    ]
