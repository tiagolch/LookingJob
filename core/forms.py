from django.forms import HiddenInput
from .models import Companies, Documents
from django import forms


class CompaniesForms(forms.ModelForm):
    class Meta:
        model = Companies
        fields = [
            'user',
            'name',
            'position',
            'contact',
            'email',
            'submition_date',
            'interview_date',
            'document_send',
            'aplication_status',
            'active',
            'link',
            'obs',
        ]
        widgets = {
            'user': HiddenInput()
        }


    def __init__(self, user=None, *args, **kwargs):
        super(CompaniesForms, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.initial['user'] = user
        else:
            print('Não autenticado')