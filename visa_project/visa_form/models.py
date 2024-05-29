from django.db import models

# Create your models here.



class VisaApplication(models.Model):
    full_name = models.CharField(max_length=255)
    mothers_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    previous_nationality = models.CharField(max_length=255)
    present_nationality = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    religion = models.CharField(max_length=50)
    sect = models.CharField(max_length=50)
    profession = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    home_address = models.TextField()
    business_address = models.TextField()
    purpose_of_travel = models.CharField(max_length=50)
    passport_no = models.CharField(max_length=50)
    passport_date_of_issue = models.DateField()
    passport_place_of_issue = models.CharField(max_length=255)
    passport_expiry_date = models.DateField()
    date_of_departure = models.DateField()
    date_of_arrival = models.DateField()
    duration_of_stay = models.IntegerField()
    method_of_payment = models.CharField(max_length=50)
    destination = models.CharField(max_length=255)
    carrier_name = models.CharField(max_length=255)
    dependents = models.TextField(blank=True, null=True)
    company_name_or_person = models.TextField()
    signature = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.full_name
