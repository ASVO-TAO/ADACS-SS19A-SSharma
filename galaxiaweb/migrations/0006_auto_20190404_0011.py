# Generated by Django 2.1.7 on 2019-04-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxiaweb', '0005_auto_20190403_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobparameter',
            name='magnitude_name_1',
            field=models.CharField(choices=[('Placeholder', 'Placeholder')], default='Placeholder', max_length=55),
        ),
        migrations.AddField(
            model_name='jobparameter',
            name='magnitude_name_2',
            field=models.CharField(choices=[('Placeholder', 'Placeholder')], default='Placeholder', max_length=55),
        ),
    ]
