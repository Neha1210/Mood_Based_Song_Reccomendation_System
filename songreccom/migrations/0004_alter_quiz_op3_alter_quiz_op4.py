# Generated by Django 4.0 on 2023-02-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songreccom', '0003_quiz_op5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='op3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='op4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
