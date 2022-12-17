from rest_framework.viewsets import ModelViewSet
from .serializers import DocumentSerializer, AppliedCompanieSerializer
from core.models import Documents, AppliedCompanies


class DocumentViewset(ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer


class AppliedCompanyViewset(ModelViewSet):
    queryset = AppliedCompanies.objects.all()
    serializer_class = AppliedCompanieSerializer

