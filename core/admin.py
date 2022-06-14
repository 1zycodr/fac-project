from django.contrib import admin
from core import models


@admin.register(models.FuncAcceptanceCertificate)
class FuncAcceptanceCertificateModelAdmin(admin.ModelAdmin):
	pass


@admin.register(models.SystemList)
class SystemListModelAdmin(admin.ModelAdmin):
	pass
