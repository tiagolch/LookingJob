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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.CharField(max_length=150, blank=True, verbose_name='Documento(s)')

    def __str__(self) -> str:
        return self.document

    class Meta:
        verbose_name_plural = 'Documents'


class Processes(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    describe = models.CharField('Process', max_length=100)
    active = models.BooleanField(default=True,verbose_name='Ativo')

    def __str__(self):
        return self.describe

    class Meta:
        verbose_name = 'Process'
        verbose_name_plural = 'Processes'


class Interviews(models.Model):
    interview_date = models.DateTimeField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.interview_date.strftime('%d/%m/%Y %H:%M') 

    class Meta:
        verbose_name = 'interview'
        verbose_name_plural = 'interviews'


class AppliedCompanies(Base):

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
    interviews = models.ForeignKey(Interviews, on_delete=models.CASCADE, null=True, blank=True)
    document_send = models.ManyToManyField(
        Documents, 
        related_name="documents_send", 
        blank=True,
        null=True,
        verbose_name='Documento(s) enviado'    
    )
    active = models.BooleanField(default=True,verbose_name='Ativo')
    link = models.URLField(max_length=500, blank=True, null=True)
    process = models.ForeignKey(Processes, on_delete=models.CASCADE)
    obs = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.position}'

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = 'Applied Company'
        verbose_name_plural = 'Applied Companies'








