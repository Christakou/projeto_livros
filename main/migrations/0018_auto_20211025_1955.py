# Generated by Django 3.1.7 on 2021-10-25 19:55

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210403_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='media/faustao.jpg', force_format='JPEG', keep_meta=True, null=True, quality=100, size=[300, 300], upload_to=''),
        ),
    ]