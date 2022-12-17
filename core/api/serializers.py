from rest_framework.serializers import ModelSerializer
from core.models import Documents, AppliedCompanies, Processes, Interviews

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class AppliedCompanieSerializer(ModelSerializer):
    class Meta:
        model = AppliedCompanies
        fields = '__all__'


class ProcessesCompanieSerializer(ModelSerializer):
    class Meta:
        model = Processes
        fields = '__all__'

class InterviewsCompanieSerializer(ModelSerializer):
    class Meta:
        model = Interviews
        fields = '__all__'