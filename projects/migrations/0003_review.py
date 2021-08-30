# Generated by Django 3.0.1 on 2021-08-24 01:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210824_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'up'), ('down', 'down')], max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]
