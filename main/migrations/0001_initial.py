# Generated by Django 2.2.3 on 2019-07-16 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('meta_description', models.TextField(blank=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('meta_description', models.TextField(blank=True)),
                ('entrance_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_display', models.BooleanField(default=True, verbose_name='Display')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='places', to='main.Category')),
            ],
            options={
                'ordering': ['-created'],
                'index_together': {('id', 'slug')},
            },
        ),
    ]