# Generated by Django 4.0 on 2022-02-06 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itask', '0004_alter_contributors_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings_points',
            name='related_contributor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itask.contributors'),
        ),
    ]