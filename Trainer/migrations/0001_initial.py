# Generated by Django 3.0b1 on 2019-12-03 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GovernmentEmployee', '0002_auto_20191128_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TopicName', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('TrainingName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GovernmentEmployee.Training')),
            ],
            options={
                'db_table': 'topic',
            },
        ),
        migrations.CreateModel(
            name='ShortQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShortQuestionName', models.TextField(default='', max_length=250)),
                ('TopicName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trainer.Topic')),
            ],
            options={
                'db_table': 'ShortQuestion',
            },
        ),
    ]
