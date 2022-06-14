from django.views.generic import (
	ListView, CreateView
)
from core import models


class FACListView(ListView):
	model = models.FuncAcceptanceCertificate
	queryset = models.FuncAcceptanceCertificate.objects.all()
	template_name = 'fac/index.html'


class SystemListView(ListView):
	model = models.SystemList
	queryset = models.SystemList.objects.all()
	template_name = 'system/index.html'
