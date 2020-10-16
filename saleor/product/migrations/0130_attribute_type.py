# Generated by Django 3.1 on 2020-10-09 10:17

from django.db import migrations, models


def set_product_type_to_all_existing_attributes(apps, schema_editor):
    Attribute = apps.get_model("product", "Attribute")
    Attribute.objects.all().update(type="product-type")


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0129_add_product_types_and_attributes_perm"),
    ]

    operations = [
        migrations.AddField(
            model_name="attribute",
            name="type",
            field=models.CharField(
                choices=[("product-type", "Product type"), ("page-type", "Page type")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.RunPython(
            set_product_type_to_all_existing_attributes, migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="attribute",
            name="type",
            field=models.CharField(
                choices=[("product-type", "Product type"), ("page-type", "Page type")],
                max_length=50,
            ),
        ),
    ]