from django.db import models


class SystemList(models.Model):

	class Meta:
		verbose_name = 'Системный список'
		verbose_name_plural = 'Системные списки'

	name = models.CharField(
		max_length=255,
		verbose_name='Наименование объекта'
	)

	type = models.CharField(
		max_length=255,
		verbose_name='Тип'
	)

	date = models.DateField(
		verbose_name='Дата'
	)

	def __str__(self):
		return f'{self.name}'


class FuncAcceptanceCertificate(models.Model):

	class Meta:
		verbose_name = 'Функционально приёмочный акт'
		verbose_name_plural = 'Функционально приёмочные акты'

	number = models.CharField(
		max_length=255,
		verbose_name='Номер'
	)

	protocol = models.CharField(
		max_length=255,
		verbose_name='Протокол тестирования'
	)

	description = models.CharField(
		max_length=255,
		verbose_name='Описание патча'
	)

	objs = models.TextField(
		blank=True,
		verbose_name='Объекты'
	)

	date = models.DateField(
		verbose_name='Дата посадки'
	)

	customer = models.CharField(
		max_length=255,
		verbose_name='Заказчик'
	)

	executor = models.CharField(
		max_length=255,
		verbose_name='Исполнитель'
	)

	def __str__(self):
		return f'№{self.number}, {self.description}'
