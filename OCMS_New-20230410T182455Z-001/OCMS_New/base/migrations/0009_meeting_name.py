# Generated by Django 3.2.12 on 2023-04-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_meeting_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='name',
            field=models.CharField(default='default', max_length=400, null=True),
        ),
    ]
