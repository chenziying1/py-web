# Generated by Django 4.1.4 on 2023-07-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jianli', '0004_contact_gongzhuojingli_contact_jiaoyubeijing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
