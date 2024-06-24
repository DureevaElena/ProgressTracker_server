# Generated by Django 5.0.6 on 2024-06-22 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecategorytodo', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DoneTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namedonetodo', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatusTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namestatustodo', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NoteTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titletodo', models.CharField(max_length=56)),
                ('notetodo', models.TextField(blank=True, max_length=500, null=True)),
                ('note_picturetodo', models.ImageField(blank=True, null=True, upload_to='')),
                ('dataendtodo', models.DateField(blank=True, null=True)),
                ('authortodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cattodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.categorytodo')),
                ('statustodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.statustodo')),
            ],
        ),
        migrations.CreateModel(
            name='StageNoteTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlestagetodo', models.CharField(max_length=56)),
                ('notestagetodo', models.TextField(blank=True, max_length=500, null=True)),
                ('authorstagetodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('donetodo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.donetodo')),
                ('idnotetodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idnoteisstage', to='todo.notetodo')),
            ],
        ),
    ]
