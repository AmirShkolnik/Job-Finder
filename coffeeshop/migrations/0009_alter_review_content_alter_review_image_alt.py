# Generated by Django 4.2.11 on 2024-05-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coffeeshop", "0008_alter_review_coffee_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="content",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="review",
            name="image_alt",
            field=models.CharField(default="Coffee Shop Image", max_length=100),
        ),
    ]