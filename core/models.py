from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Base(models.Model):
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y %H:%M') 

    def get_updated_at(self):
        return self.updated_at.strftime('%d/%m/%Y %H:%M') 


class Documents(Base):
    document = models.CharField(max_length=150, blank=True, verbose_name='Documento(s)')

    def __str__(self) -> str:
        return self.document

    class Meta:
        verbose_name_plural = 'Documents'


class Companies(Base):
    APLICATION_STATUS_CHOICES = [
        ('AGUARDANDO CONTATO', 'AGUARDANDO CONTATO'),
        ('REJEITADO', 'REJEITADO'),
        ('EM ANALISE', 'EM ANALISE'),
        ('PROXIMA ENTREVISTA', 'PROXIMA ENTREVISTA'),
        ('ACEITO', 'ACEITO'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=150, verbose_name='Empresa')
    position = models.CharField(
        max_length=100, 
        help_text='Sobre a posição da vaga', 
        verbose_name='Vaga'
    )
    contact = models.CharField(
        max_length=100, 
        verbose_name='Recrutador', 
        blank=True, 
        null=True
    )
    email = models.EmailField(blank=True)
    submition_date = models.DateField(
        default=date.today(), 
        blank=True, 
        verbose_name='Data de inscrição'
    )
    interview_date = models.DateTimeField( 
        blank=True, 
        null=True,
        verbose_name='Data da entrevista'
    )
    document_send = models.ManyToManyField(
        Documents, 
        related_name="documents_send", 
        blank=True,
        null=True,
        verbose_name='Documento(s) enviado'    
    )
    aplication_status = models.CharField(
        max_length=20, 
        choices=APLICATION_STATUS_CHOICES, 
        default='AGUARDANDO_CONTATO',
        verbose_name='Status'
    )
    active = models.BooleanField(default=True,verbose_name='Ativo')
    link = models.URLField(max_length=500, blank=True, null=True)
    process = models.ForeignKey(Processes, on_delete=models.CASCADE)
    obs = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.position}'

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'








