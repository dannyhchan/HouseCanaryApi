# Generated by Django 4.1.4 on 2022-12-29 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('questionId', models.IntegerField()),
                ('answer', models.CharField(max_length=200)),
                ('propertyId', models.IntegerField()),
            ],
        ),
    ]
