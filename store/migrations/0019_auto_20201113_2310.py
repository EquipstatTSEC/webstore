# Generated by Django 3.1.2 on 2020-11-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20201103_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productnew',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='NewProducts/'),
        ),
        migrations.AlterField(
            model_name='productrefurbished',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='RefurbishedProducts/'),
        ),
    ]