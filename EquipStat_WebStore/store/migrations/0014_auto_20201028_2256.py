# Generated by Django 3.1.1 on 2020-10-28 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0013_auto_20201028_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrefurbished',
            name='sellerID',
        ),
        migrations.AlterField(
            model_name='productrefurbished',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
