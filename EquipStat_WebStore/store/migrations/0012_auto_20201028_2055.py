# Generated by Django 3.1.1 on 2020-10-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20201025_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrefurbished',
            name='sellerID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
