# Generated by Django 4.1.7 on 2023-03-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_mohtava'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mohtava',
            options={'verbose_name_plural': 'mohtavas'},
        ),
        migrations.AddField(
            model_name='mohtava',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
