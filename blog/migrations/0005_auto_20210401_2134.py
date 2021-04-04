# Generated by Django 3.1.3 on 2021-04-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('---Select---', '---Select---'), ('Food', 'Food'), ('Music', 'Music'), ('Nature', 'Nature'), ('Education', 'Education'), ('Wedding', 'Wedding'), ('Travel', 'Travel'), ('Movie', 'Movie'), ('Car', 'Car'), ('Project', 'Project'), ('Photography', 'Photography'), ('Other', 'Other')], default='---Select---', max_length=20),
        ),
    ]