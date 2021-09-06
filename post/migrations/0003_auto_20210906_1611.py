# Generated by Django 3.2.7 on 2021-09-06 16:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210906_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='randurl',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='rndid',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100, null=True),
        ),
    ]
