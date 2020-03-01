# Generated by Django 2.2.3 on 2020-02-04 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignmentApi', '0006_delete_survey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surveyId', models.IntegerField()),
                ('assignment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='assignmentApi.AssignmentChoices')),
                ('survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey', to='assignmentApi.Assignment')),
            ],
        ),
    ]
