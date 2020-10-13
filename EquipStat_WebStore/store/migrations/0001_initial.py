# Generated by Django 3.1.2 on 2020-10-13 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mrp', models.FloatField()),
                ('ourPrice', models.FloatField()),
                ('inventory', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academicDetails', models.TextField()),
                ('contact', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductRefurbished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('typeOfProduct', models.CharField(choices=[('1', 'Books'), ('2', 'Lab Coats'), ('3', 'Instruments')], max_length=20)),
                ('expectedReturn', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('details', models.TextField()),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.userdetails')),
            ],
        ),
    ]
