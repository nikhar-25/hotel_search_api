# Generated by Django 4.2.7 on 2023-12-01 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Amenities",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amenity", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hotel_name", models.CharField(max_length=100)),
                ("hotel_price", models.IntegerField()),
                ("hotel_description", models.TextField()),
                ("banner_image", models.ImageField(upload_to="hotels")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("amenities", models.ManyToManyField(to="home.amenities")),
            ],
        ),
        migrations.CreateModel(
            name="HotelImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="hotels")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.hotel"
                    ),
                ),
            ],
        ),
    ]
