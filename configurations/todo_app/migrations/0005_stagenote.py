# Generated by Django 5.0.6 on 2024-06-17 19:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_category_note_cat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StageNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlestage', models.CharField(max_length=56)),
                ('notestage', models.TextField(max_length=500)),
                ('authorstage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('catstage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo_app.category')),
                ('idnote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idnoteisstage', to='todo_app.note')),
            ],
        ),
    ]
