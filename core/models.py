from django.db import models
from datetime import date
from datetime import datetime


class Base(models.Model):
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y %H:%M') 

    def get_updated_at(self):
        return self.updated_at.strftime('%d/%m/%Y %H:%M') 


class Companies(Base):
    APLICATION_STATUS_CHOICES = [
        ('AGUARDANDO_CONTATO', 'AGUARDANDO CONTATO'),
        ('REJEITADO', 'REJEITADO'),
        ('EM_ANALISE', 'EM ANALISE'),
        ('PROXIMA_ENTREVISTA', 'PROXIMA ENTREVISTA'),
        ('ACEITO', 'ACEITO'),
    ]

    name = models.CharField( max_length=150, verbose_name='Company')
    position = models.CharField(max_length=100, help_text='Sobre a posição da vaga')
    contact = models.CharField(max_length=100, verbose_name='Contact Name')
    email = models.EmailField(blank=True)
    submition_date = models.DateField(default=date.today(), blank=True)
    interview_date = models.DateField( 
        blank=True, 
        null=True,
        help_text='Data da entrevista'
    )
    document_send = models.ManyToManyField(
        'Documents', 
        related_name="documents_send", 
        blank=True,
        null=True       
    )
    aplication_status = models.CharField(
        max_length=20, 
        choices=APLICATION_STATUS_CHOICES, 
        default='AGUARDANDO_CONTATO'
    )
    active = models.BooleanField(default=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    obs = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.position}'

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Documents(Base):
    document = models.CharField(max_length=150, blank=True)

    def __str__(self) -> str:
        return self.document

    class Meta:
        verbose_name_plural = 'Documents'




