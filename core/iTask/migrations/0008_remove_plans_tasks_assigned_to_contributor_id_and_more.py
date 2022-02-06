# Generated by Django 4.0 on 2022-02-06 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itask', '0007_plans_task_id_alter_tasks_activity_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans_tasks',
            name='assigned_to_contributor_id',
        ),
        migrations.RemoveField(
            model_name='plans_tasks',
            name='completion_status_id',
        ),
        migrations.RemoveField(
            model_name='plans_tasks',
            name='plan_id',
        ),
        migrations.RemoveField(
            model_name='plans_tasks',
            name='priority_id',
        ),
        migrations.RemoveField(
            model_name='plans_tasks',
            name='task_id',
        ),
        migrations.AddField(
            model_name='tasks',
            name='assigned_to_contributor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to_contributor_id', to='itask.contributors'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='priority_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='itask.priorities'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='retro_remarks',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='completed_by_contibutor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_by_contibutor_id', to='itask.contributors'),
        ),
        migrations.DeleteModel(
            name='plans',
        ),
        migrations.DeleteModel(
            name='plans_tasks',
        ),
    ]
