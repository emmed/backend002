# Generated by Django 3.0.6 on 2020-05-30 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0009_add_subregion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=800, null=True)),
                ('image', models.ImageField(blank=True, max_length=250, null=True, upload_to='post_image')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=200, null=True)),
                ('answer', models.TextField(max_length=800, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(choices=[('No major', 'No major'), ('Handelsingenieur', 'Handelsingenieur'), ('Industriële wetenschappen Energie', 'Industriële wetenschappen Energie'), ('Biowetenschappen', 'Biowetenschappen'), ('Architectuur', 'Architectuur'), ('International Business', 'International Business'), ('Fysica', 'Fysica'), ('Wiskunde', 'Wiskunde'), ('Wijsbegeerte', 'Wijsbegeerte'), ('Kunstwetenschappen', 'Kunstwetenschappen'), ('Taal- en letterkunde', 'Taal- en letterkunde'), ('Geologie', 'Geologie'), ('Informatica', 'Informatica'), ('Rechten', 'Rechten'), ('Geschiedenis', 'Geschiedenis'), ('Beeldende kunsten', 'Beeldende kunsten'), ('Visual Arts', 'Visual Arts'), ('Drama', 'Drama'), ('Muziek', 'Muziek'), ('Chemie', 'Chemie'), ('Biomedische laboratoriumtechnologie', 'Biomedische laboratoriumtechnologie'), ('Bedrijfsmanagement', 'Bedrijfsmanagement'), ('Journalistiek', 'Journalistiek'), ('Office management', 'Office management'), ('Transport en logistiek', 'Transport en logistiek')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=800, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, max_length=250, null=True, upload_to='post_image')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restapi.Category')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.City')),
                ('condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restapi.Condition')),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restapi.Major')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(choices=[('No school', 'No school'), ('Odisee', 'Odisee'), ('LUCA School of Arts', 'LUCA School of Arts'), ('Erasmushogeschool Brussel', 'Erasmushogeschool Brussel'), ('Artesis Plantijn Hogeschool', 'Artesis Plantijn Hogeschool'), ('Karel de Grote-Hogeschool', 'Karel de Grote-Hogeschool'), ('Thomas More', 'Thomas More'), ('UC Leuven', 'UC Leuven'), ('Hogeschool PXL', 'Hogeschool PXL'), ('UC Limburg', 'UC Limburg'), ('Hogeschool West-Vlaanderen', 'Hogeschool West-Vlaanderen'), ('Katholieke Hogeschool Vives', 'Katholieke Hogeschool Vives'), ('Hogeschool Gent Geraard', 'Hogeschool Gent\tGeraard'), ('Arteveldehogeschool', 'Arteveldehogeschool'), ('Vrije Universiteit Brussel', 'Vrije Universiteit Brussel'), ('Universiteit Antwerpen', 'Universiteit Antwerpen'), ('Katholieke Universiteit Leuven', 'Katholieke Universiteit Leuven'), ('Universiteit Hasselt', 'Universiteit Hasselt'), ('Universiteit Gent', 'Universiteit Gent')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('No subject', 'No subject'), ('Wiskunde', 'Wiskunde'), ('Algoritmes', 'Algoritmes'), ('Analyses', 'Analyses'), ('Informatica', 'Informatica'), ('Fysica', 'Fysica'), ('Wijsbegeerte', 'Wijsbegeerte'), ('Geologie', 'Geologie'), ('Psychologie', 'Psychologie'), ('Godsdienst', 'Godsdienst'), ('Frans', 'Frans'), ('Engels', 'Engels'), ('Duits', 'Duits'), ('Biologie', 'Biologie'), ('Toerisme', 'Toerisme'), ('Economie', 'Economie'), ('Toneel', 'Toneel'), ('Audiovisuele vorming', 'Audiovisuele vorming')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restapi.Product')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restapi.School'),
        ),
        migrations.AddField(
            model_name='product',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restapi.Subject'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('user', 'title')},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('user', 'title')},
        ),
    ]
