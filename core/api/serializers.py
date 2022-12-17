from rest_framework.serializers import ModelSerializer
from core.models import Documents, AppliedCompanies

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class AppliedCompanieSerializer(ModelSerializer):
    class Meta:
        model = AppliedCompanies
        fields = '__all__'