from django.db import models

class SalesPerson(models.Model):
    SalesPersonI_ID = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)

class SalesInvoice(models.Model):
    Invoice_ID = models.AutoField(primary_key=True)
    Invoice_Number = models.CharField(max_length=50)
    Date = models.DateField()
    CustomerID = models.CharField(max_length=50)
    SalesPerson_ID = models.ForeignKey(SalesPerson, on_delete=models.CASCADE)
    Car_ID = models.AutoField(foreign_key=True)
class Car_ID(models.Model):
    SerialNumber = models.CharField(max_length=50)
    Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Colour = models.CharField(max_length=50)
    Year = models.CharField(max_length=50)
    CarForSale = models.BoolField(max_length=50)

class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    PostalCode=models.CharField(max_length=50)

class Mechanic(models.Model):
    Mechanic_ID = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)

class ServiceMechanic(models.Model):
    ServiceMechanic_ID = models.AutoField(primary_key=True)
    ServiceTicket_ID = models.AutoField(foreign_key=True)
    MechanicName = models.AutoField(foreign_key=True)
    Hours = models.IntegerField()
    Comment =models.CharField(max_length=50)
    Rate=models.IntegerField()

class ServiceTicket(models.Model):
    ServiceTicket_ID = models.AutoField(primary_key=True)
    ServiceTicketNumber = models.CharField(max_length=50)
    Car_ID = models.ForeignKey(Car_ID, on_delete=models.CASCADE)
    DateReceived = models.DateField()
    Comments = models.CharField(max_length=50)
    DateReturnedToCustomer = models.DateField()

class Service(models.Model):
    Service_ID = models.AutoField(primary_key=True)
    ServiceName = models.CharField(max_length=50)
    HourlyRate = models.IntegerField()

class Parts(models.Model):
    Parts_ID = models.AutoField(primary_key=True)
    PartNumber = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    PurchasePrice = models.IntegerField()
    RetailPrice = models.IntegerField()

class PartsUsed(models.Model):
    PartsUsed_ID = models.AutoField(primary_key=True)
    ServiceTicketID = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    NumberUsed=models.IntegerField()
    Price = models.IntegerField()