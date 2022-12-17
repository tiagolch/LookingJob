from django.forms import HiddenInput
from .models import AppliedCompanies, Documents, Processes
from django import forms


class AppliedCompaniesForms(forms.ModelForm):
    class Meta:
        model = AppliedCompanies
        fields = [
            'user',
            'name',
            'position',
            'contact',
            'email',
            'submition_date',
            'interviews',
            'document_send',
            'active',
            'link',
            'process',
            'obs',
        ]
        widgets = {
            'user': HiddenInput()
        }


    def __init__(self, user=None, *args, **kwargs):
        super(AppliedCompaniesForms, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.initial['user'] = user
        else:
            print('Não autenticado')