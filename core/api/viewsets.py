from rest_framework.viewsets import ModelViewSet
from .serializers import (
    DocumentSerializer, 
    AppliedCompanieSerializer, 
    ProcessesCompanieSerializer, 
    InterviewsCompanieSerializer
)
from core.models import Documents, AppliedCompanies, Processes, Interviews


class DocumentViewset(ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer


class AppliedCompanyViewset(ModelViewSet):
    queryset = AppliedCompanies.objects.all()
    serializer_class = AppliedCompanieSerializer


class ProcessesViewset(ModelViewSet):
    queryset = Processes.objects.all()
    serializer_class = ProcessesCompanieSerializer


class InterviewsViewset(ModelViewSet):
    queryset = Interviews.objects.all()
    serializer_class = InterviewsCompanieSerializer