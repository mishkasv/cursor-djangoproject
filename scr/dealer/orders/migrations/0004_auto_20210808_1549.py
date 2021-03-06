# Generated by Django 3.2.5 on 2021-08-08 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='some@some', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.TextField(default='some message'),
            preserve_default=False,
        ),
    ]
