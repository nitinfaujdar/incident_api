# Generated by Django 3.2.4 on 2023-07-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramognee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reporter_name', models.CharField(max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country_code',
            field=models.CharField(help_text='Optional: country code format +91', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('ENTERPRISE', 'Enterprise'), ('GOVERNMENT', 'Government')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_phone_no',
            field=models.CharField(help_text='Optional: phone number format 8130514811.', max_length=20, null=True),
        ),
    ]