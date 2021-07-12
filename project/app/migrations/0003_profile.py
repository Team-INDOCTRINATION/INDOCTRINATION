# Generated by Django 3.2.4 on 2021-07-12 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0002_rename_customer_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(default='', max_length=50)),
                ('address', models.CharField(max_length=70)),
                ('phoneNo', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=20)),
                ('registeredAt', models.DateTimeField(auto_now_add=True)),
                ('dob', models.DateField()),
                ('disability', models.CharField(blank=True, max_length=10, null=True)),
                ('bio', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
