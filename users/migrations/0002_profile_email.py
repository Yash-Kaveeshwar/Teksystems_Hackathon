# Generated by Django 2.2.2 on 2019-06-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='chouhan.gir@gmail.com', max_length=254),
        ),
    ]
