# Generated by Django 3.0.2 on 2020-01-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
