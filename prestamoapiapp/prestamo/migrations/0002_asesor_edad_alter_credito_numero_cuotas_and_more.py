# Generated by Django 4.1.6 on 2023-03-26 15:57

from django.db import migrations, models
import django.db.models.deletion
import prestamo.validators


class Migration(migrations.Migration):
    dependencies = [
        ("prestamo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="asesor",
            name="edad",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                max_digits=10,
                validators=[prestamo.validators.edad],
            ),
        ),
        migrations.AlterField(
            model_name="credito",
            name="numero_cuotas",
            field=models.PositiveIntegerField(
                validators=[prestamo.validators.validar_par]
            ),
        ),
        migrations.AlterField(
            model_name="credito",
            name="total",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, validators=[prestamo.validators.monto]
            ),
        ),
        migrations.AlterField(
            model_name="tipodecredito",
            name="nombre",
            field=models.CharField(
                max_length=100, validators=[prestamo.validators.validation_tipo_credito]
            ),
        ),
        migrations.CreateModel(
            name="Cuota",
            fields=[
                ("id_cuota", models.AutoField(primary_key=True, serialize=False)),
                ("total", models.DecimalField(decimal_places=2, max_digits=100)),
                ("fecha", models.DateField()),
                (
                    "id_tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="prestamo.tipodecredito",
                    ),
                ),
            ],
        ),
    ]
