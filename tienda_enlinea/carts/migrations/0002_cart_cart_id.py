# Generated by Django 3.1.2 on 2020-10-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
