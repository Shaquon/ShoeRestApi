# Generated by Django 3.0.1 on 2020-01-02 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_style', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=1, max_digits=3)),
                ('brand', models.CharField(max_length=75)),
                ('material', models.CharField(max_length=75)),
                ('fasten_type', models.CharField(max_length=50)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.ShoeType')),
            ],
        ),
    ]
