from django import forms

from core import models


class CreateFuncAcceptanceCertificate(forms.ModelForm):

	class Meta:
		model = models.FuncAcceptanceCertificate
		fields = '__all__'


class EditFuncAcceptanceCertificate(forms.ModelForm):

	class Meta:
		model = models.FuncAcceptanceCertificate
		fields = '__all__'
