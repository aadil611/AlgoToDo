# Generated by Django 4.2.1 on 2023-06-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="status",
            field=models.CharField(
                choices=[
                    ("open", "Open"),
                    ("working", "Working"),
                    ("done", "Done"),
                    ("overdue", "Overdue"),
                ],
                default="open",
                max_length=20,
                null=True,
            ),
        ),
    ]
