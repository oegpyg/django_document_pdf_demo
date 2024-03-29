# Generated by Django 4.0.4 on 2024-02-10 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhantasyName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Logo', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=20, unique=True)),
                ('Description', models.CharField(max_length=50)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PayTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaxRegNr', models.CharField(max_length=20)),
                ('StartDate', models.DateField()),
                ('DueDate', models.DateField()),
                ('SerialNumber', models.CharField(max_length=100)),
                ('DeliveryAddress', models.CharField(max_length=100)),
                ('DeliveryDate', models.DateField()),
                ('Comments', models.TextField()),
                ('SubTotal', models.IntegerField()),
                ('TaxTotal', models.IntegerField()),
                ('Total', models.IntegerField()),
                ('TotalInText', models.CharField(max_length=100)),
                ('User', models.CharField(max_length=20)),
                ('Computer', models.CharField(max_length=20)),
                ('TransactionDate', models.DateTimeField()),
                ('InvoiceDate', models.DateTimeField()),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.company')),
                ('PayTerm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.payterm')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=20)),
                ('TaxRegNr', models.CharField(max_length=20)),
                ('PhantasyName', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('Address', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('ContactName', models.CharField(max_length=100)),
                ('ContactNumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseInvoiceItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Quantity', models.IntegerField()),
                ('SubTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.item')),
                ('PurchaseInvoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.purchaseinvoice')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseinvoice',
            name='Supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.supplier'),
        ),
    ]
