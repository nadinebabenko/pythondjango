# Generated by Django 4.2.4 on 2023-09-25 15:37

from django.db import migrations, models

migrations.AddField(
    model_name='todo',
    name='category',
    field=models.CharField(default='default_category', max_length=100),
)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('has_been_done', models.BooleanField(default=False)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_completion', models.DateTimeField(blank=True, null=True)),
                ('deadline_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
