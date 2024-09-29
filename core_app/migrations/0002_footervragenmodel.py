# Generated by Django 5.1 on 2024-09-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterVragenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('vraag-1', 'Vraag 1'), ('vraag-2', 'Vraag 2'), ('vraag-3', 'Vraag 3')], max_length=50)),
                ('question', models.TextField(help_text='Vul hier je vraag of opmerking in.', max_length=250)),
            ],
        ),
    ]
