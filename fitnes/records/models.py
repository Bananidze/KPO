from django.db import models

class Record(models.Model):
    doctor = models.CharField('Врач', max_length=50)
    patient = models.CharField('Пациент', max_length=50)
    diagnos = models.TextField('Диагноз')
    date = models.DateTimeField('Дата записи')

    def __str__(self):
        return self.patient
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'