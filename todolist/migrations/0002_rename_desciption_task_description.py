# Generated by Django 4.1 on 2022-09-24 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="desciption", new_name="description",
        ),
    ]
