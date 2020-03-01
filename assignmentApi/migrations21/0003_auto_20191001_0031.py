# Generated by Django 2.2.3 on 2019-10-01 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignmentApi', '0002_auto_20191001_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentchoices',
            name='assignment_choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='assignmentApi.Assignment'),
        ),
        migrations.AddField(
            model_name='survey',
            name='assignment_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='assignmentApi.AssignmentChoices'),
        ),
        migrations.AddField(
            model_name='survey',
            name='survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='assignmentApi.Assignment'),
        ),
        migrations.AlterField(
            model_name='gradedassignment',
            name='assignmentcompleted',
            field=models.BooleanField(default=False),
        ),
    ]
