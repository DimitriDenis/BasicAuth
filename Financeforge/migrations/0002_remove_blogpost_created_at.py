# Generated by Django 5.0.1 on 2024-01-16 14:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Financeforge", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="created_at",
        ),
    ]