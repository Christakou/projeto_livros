# Generated by Django 3.1.7 on 2021-03-13 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='recommended_books',
            field=models.ManyToManyField(null=True, related_name='influencer_who_recommends', to='main.Book'),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='written_books',
            field=models.ManyToManyField(null=True, related_name='influencer_who_wrote', to='main.Book'),
        ),
    ]
