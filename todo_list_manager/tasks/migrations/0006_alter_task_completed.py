# Generated by Django 4.2.7 on 2024-08-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_category_alter_task_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=True),
        ),
    ]
