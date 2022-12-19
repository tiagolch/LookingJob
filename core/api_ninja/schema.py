from datetime import date
from core.models import Companies
from ninja import Schema, ModelSchema
from typing import Optional, List


class UserSchema(Schema):
    id: int
    username: str
    first_name: str
    last_name: str


class DocumentsSchema(Schema):
    id: int
    document: str


class CompaniesSchema(ModelSchema):
    user: UserSchema
    document_send: List[DocumentsSchema] = []
    class Config:
        model = Companies
        model_fields = "__all__"
