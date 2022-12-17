from rest_framework.serializers import ModelSerializer
from core.models import Documents, Companies

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class CompanieSerializer(ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'