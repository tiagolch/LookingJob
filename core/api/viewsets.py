from rest_framework.viewsets import ModelViewSet
from core.models import AppliedCompanies, Documents, Interviews, Processes
from .serializers import (AppliedCompanieSerializer, DocumentSerializer,
                          InterviewsCompanieSerializer,
                          ProcessesCompanieSerializer)


class DocumentViewset(ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user=self.request.user)
        return self.queryset
    


class AppliedCompanyViewset(ModelViewSet):
    queryset = AppliedCompanies.objects.all()
    serializer_class = AppliedCompanieSerializer

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user=self.request.user)
        return self.queryset


class ProcessesViewset(ModelViewSet):
    queryset = Processes.objects.all()
    serializer_class = ProcessesCompanieSerializer

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(user=self.request.user)
        return self.queryset


class InterviewsViewset(ModelViewSet):
    queryset = Interviews.objects.all()
    serializer_class = InterviewsCompanieSerializer