# Generated by Django 2.2.15 on 2020-10-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loans", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="library", options={"verbose_name_plural": "Libraries"},),
        migrations.AddField(
            model_name="library",
            name="name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
