# Generated by Django 3.1 on 2021-06-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0003_auto_20210602_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='PharmcistDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('Password', models.CharField(max_length=20, null=True)),
                ('village', models.CharField(max_length=20)),
                ('District', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
            ],
        ),
    ]
