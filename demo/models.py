from django.db import models


class Supplier(models.Model):
    Code = models.CharField(max_length=20)
    TaxRegNr = models.CharField(max_length=20)
    PhantasyName = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Address = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    ContactName = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=15)


class PayTerm(models.Model):
    Description = models.CharField(max_length=100)


class Company(models.Model):
    PhantasyName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Phone = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Logo = models.FileField(upload_to='images/', max_length=100)


class PurchaseInvoice(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    TaxRegNr = models.CharField(max_length=20)
    StartDate = models.DateField(auto_now=False, auto_now_add=False)
    DueDate = models.DateField(auto_now=False, auto_now_add=False)

    Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    SerialNumber = models.CharField(max_length=100)

    PayTerm = models.ForeignKey(PayTerm, on_delete=models.CASCADE)    
    DeliveryAddress = models.CharField(max_length=100)
    DeliveryDate = models.DateField(auto_now=False, auto_now_add=False)

    Comments = models.TextField()

    SubTotal = models.IntegerField()
    TaxTotal = models.IntegerField()
    Total = models.IntegerField()
    TotalInText = models.CharField(max_length=100)

    User = models.CharField(max_length=20)
    Computer = models.CharField(max_length=20)
    TransactionDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    InvoiceDate = models.DateTimeField(auto_now=False, auto_now_add=False)


class Item(models.Model):
    Code = models.CharField(max_length=20, unique=True)
    Description = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=10, decimal_places=2)


class PurchaseInvoiceItems(models.Model):
    PurchaseInvoice = models.ForeignKey(
        PurchaseInvoice, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity = models.IntegerField()
    SubTotal = models.DecimalField(max_digits=10, decimal_places=2)
