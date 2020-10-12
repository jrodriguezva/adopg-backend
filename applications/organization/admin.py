from django.contrib import admin
from .models import Organization, Hour, Address, SocialMedia


admin.site.register(Organization)
admin.site.register(Hour)
admin.site.register(Address)
admin.site.register(SocialMedia)
