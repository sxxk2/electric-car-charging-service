# Generated by Django 4.1.6 on 2023-03-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentmethod",
            name="bank_account",
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="bank_name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("kookmin", "KB국민은행"),
                    ("shinhan", "신한은행"),
                    ("woori", "우리은행"),
                    ("hana", "KEB하나은행"),
                    ("nh", "농협"),
                    ("city", "시티은행"),
                    ("kakao", "카카오뱅크"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="card_number",
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]