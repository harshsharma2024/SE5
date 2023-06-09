# Generated by Django 3.2.12 on 2023-04-08 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_lectures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Tassignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('file', models.FileField(upload_to='tassignments/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.teacher')),
            ],
        ),
    ]
