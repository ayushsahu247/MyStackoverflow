# Generated by Django 4.0.4 on 2022-04-26 18:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePost',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('text', ckeditor.fields.RichTextField()),
                ('media', models.TextField(blank=True, null=True)),
                ('upvote_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('name', models.CharField(max_length=100)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.basepost')),
                ('title', models.TextField()),
                ('tags', models.ManyToManyField(to='posts.tag')),
            ],
            bases=('posts.basepost',),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.basepost')),
                ('this_worked', models.BooleanField(default=False)),
                ('question_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.question')),
            ],
            bases=('posts.basepost',),
        ),
    ]