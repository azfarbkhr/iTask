# Generated by Django 4.0 on 2022-05-18 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pushup_logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercize_date', models.DateField(auto_now_add=True)),
                ('pushup_count', models.IntegerField()),
            ],
        ),
    ]