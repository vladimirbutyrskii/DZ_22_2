# Generated by Django 5.1 on 2024-08-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_manufactured_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="views_counter",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Укажите количество просмотров",
                verbose_name="Счетчик просмотров",
            ),
        ),
    ]
