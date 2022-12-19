from typing import List
from ninja import NinjaAPI
from core.models import Companies
from .schema import CompaniesSchema


api = NinjaAPI()


@api.get("/list_subscriptions", response=List[CompaniesSchema])
def list_subscriptions(request):
    data = Companies.objects.all()
    return data
