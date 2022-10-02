from .models import Companies, Documents
from django import forms


class CompaniesForms(forms.ModelForm):
    class Meta:
        model = Companies
        fields = [
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