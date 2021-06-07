# Generated by Django 2.1.7 on 2021-04-30 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxiaweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobparameter',
            name='geometry_options',
            field=models.CharField(choices=[('All Sky', 'All Sky'), ('Circular Patch', 'Circular Patch')], default='Circular Patch', max_length=55),
        ),
    ]
