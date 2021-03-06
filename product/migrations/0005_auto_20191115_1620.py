# Generated by Django 2.2.7 on 2019-11-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20191114_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='obtainmethod',
            name='product_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='gluten_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Glutensiz'), (1, 'Büyük İhtimalle Yok'), (2, 'Belirsiz'), (3, 'Büyük İhtimalle Var'), (4, 'Glutenli')], default=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='gluten_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Glutensiz'), (1, 'Büyük İhtimalle Yok'), (2, 'Belirsiz'), (3, 'Büyük İhtimalle Var'), (4, 'Glutenli')], default=2),
        ),
    ]
