# Generated by Django 3.0.5 on 2020-06-22 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djaveLogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logintoken',
            name='email',
            field=models.CharField(blank=True, default='', help_text='If this email field is populated, this is a sign up link for a new user with this email address.', max_length=100),
        ),
        migrations.AlterField(
            model_name='logintoken',
            name='user',
            field=models.ForeignKey(blank=True, help_text='If this user field is populated, this is a login token for that user.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]