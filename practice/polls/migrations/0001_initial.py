# Generated by Django 4.0.1 on 2022-01-21 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='dummy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy_char', models.CharField(max_length=200)),
                ('date', models.DateTimeField(null=True)),
                ('title', models.CharField(blank=True, max_length=25)),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
