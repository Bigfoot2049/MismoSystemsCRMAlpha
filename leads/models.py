from djongo import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Customer(models.Model):

    customer_type_choice = (("New", "New"), ("Existing", "Existing"))

    services_choice = (
        ("Microsoft 365", "Microsoft 365"),
        ("Microsoft Azure", "Microsoft Azure"),
        ("AWS", "AWS"),
        ("Google Workspace", "Google Workspace"),
    )

    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    customer_type = models.CharField(choices=customer_type_choice, max_length=10)
    testimonial = models.BooleanField(default=False)
    case_study = models.BooleanField(default=False)
    services = models.CharField(choices=services_choice, max_length=20)
    renewal_date = models.DateTimeField()
    sales_person = models.ForeignKey(
        Agent, related_name="sales_person", null=True, on_delete=models.SET_NULL
    )
    customer_manager = models.ForeignKey(
        Agent, related_name="customer_manager", null=True, on_delete=models.SET_NULL
    )
    last_contact = models.DateTimeField()
    last_meeting = models.DateTimeField()
    pending_actions = models.CharField(max_length=254)
    notes = models.CharField(max_length=254)

    def __str__(self):
        return self.company_name


class Lead(models.Model):

    deal_stage_choice = (
        ("Proposal Sent", "Proposal Sent"),
        ("Meeting Done", "Meeting Done"),
        ("Trial/POC", "Trial/POC"),
        ("Finalised BOM", "Finalised BOM"),
        ("Won", "Won"),
        ("Lost", "Lost"),
    )

    services_choice = (
        ("Microsoft 365", "Microsoft 365"),
        ("Microsoft Azure", "Microsoft Azure"),
        ("AWS", "AWS"),
        ("Google Workspace", "Google Workspace"),
    )

    deal_priority_choice = (("Low", " Low"), ("Medium", "Medium"), ("High", "High"))

    customer_name = models.CharField(max_length=50)
    deal_stage = models.CharField(choices=deal_stage_choice, max_length=20)
    services = models.CharField(choices=services_choice, max_length=20)
    deal_value = models.IntegerField()
    sales_person = models.ForeignKey(
        Agent, related_name="sales_person_lead", null=True, on_delete=models.SET_NULL
    )
    deal_priority = models.CharField(choices=deal_priority_choice, max_length=20)

    def __str__(self):
        return self.customer_name
