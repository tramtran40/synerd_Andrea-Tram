from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField()
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    employer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class SubscriptionType(models.Model):
    subscriptiontypecode = models.IntegerField()
    subscriptiontypename = models.CharField(max_length=50)

class Service(models.Model):
    servicecode = models.IntegerField()
    servicename = models.CharField(max_length=50)
    description = models.TextField()
    premium = models.CharField(max_length=50)
    allocation = models.CharField(max_length=50)

class Subscriber(models.model):
    subscriberID = models.IntegerField()
    username = models.ForeignKey(UserInfor)
    subscriptiontypecode = models.ForeignKey(SubscriptionType)
    servicecode = models.ForeignKey(Service)
    requestdate = models.DateField()
    startdate = models.DateField()
    enddate = models.DateField()
    motifofcancellation = models.TextField()
    beneficiaryID = models.ForeignKey(Subscriber)

class TransferredSubscription(models.model):
    transferredID = models.IntegerField()
    transfer_from = models.TextField()
    transfer_to = models.TextField()
    request_date = models.DateField()
    transfer_date = models.DateField()
    subscriberID = models.ForeignKey(Subscriber)
    

class Office(models.Model):
    officecode = models.IntegerField()
    officename = models.CharField(max_length=50)
    attribution = models.CharField(max_length=50)

class Officer(models.model):
    officecode = models.ForeignKey(Office)
    subscriberID = models.ForeignKey(Subscriber)
    startdate = models.DateField()
    enddate = models.DateField()

class Organization(models.Model):
    organization_code = models.IntegerField()
    organization_name = models.CharField(max_length=50)
    description = models.TextField()
    date_joined = model.DateField()
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)

class OrganizationMember(models.Model):
    organization_code = models.ForeignKey(Organization)
    subscriberID = models.ForeignKey(Subscriber)
    startdate = models.DateField()
    enddate = models.DateField()
    nativecountry = models.TextField()
    citizenship = models.TextField()
    isdelegate = models.Boolean()
