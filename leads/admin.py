from django.contrib import admin
from .models import User, Agent, Customer, Lead

# Register your models here.

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Customer)
admin.site.register(Lead)
