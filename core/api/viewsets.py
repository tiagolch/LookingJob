from rest_framework.viewsets import ModelViewSet
from .serializers import DocumentSerializer, CompanieSerializer
from core.models import Documents, Companies


class DocumentViewset(ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer


class CompanyViewset(ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanieSerializer

