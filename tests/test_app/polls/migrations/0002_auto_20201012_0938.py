# Generated by Django 2.2.15 on 2020-10-12 08:38

from datetime import timedelta

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="time",
            field=models.DurationField(default=timedelta(days=1)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="choice",
            name="choice_text",
            field=models.CharField(
                choices=[("Here is a choice", "Here is a choice"), ("Here is another choice", "Here is another choice")],
                max_length=255,
            ),
        ),
    ]
