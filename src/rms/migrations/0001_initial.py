# Generated by Django 2.2.3 on 2019-12-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('birth_date', models.DateField(null=True)),
                ('experties', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('bio', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=30)),
                ('about', models.TextField(null=True)),
            ],
        ),
    ]