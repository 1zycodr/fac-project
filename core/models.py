from django.db import models


class SystemList(models.Model):

	class Meta:
		verbose_name = 'Системный список'
		verbose_name_plural = 'Системные списки'

	PROCEDURE, OBJECT, PACKAGE = range(3)

	TYPE_CHOICES = (
		(PROCEDURE, 'PROCEDURE'),
		(OBJECT, 'OBJECT'),
		(PACKAGE, 'PACKAGE'),
	)

	name = models.CharField(
		max_length=255,
		verbose_name='Наименование объекта'
	)

	type = models.IntegerField(
		choices=TYPE_CHOICES,
		verbose_name='Тип'
	)

	date = models.DateField(
		verbose_name='Дата'
	)

	def __str__(self):
		return f'{self.name}: {dict(self.TYPE_CHOICES).get(self.type)}'


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

	objs = models.ManyToManyField(
		SystemList,
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
