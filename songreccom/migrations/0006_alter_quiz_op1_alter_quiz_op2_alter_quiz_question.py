# Generated by Django 4.0 on 2023-02-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songreccom', '0005_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='op1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='op2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
