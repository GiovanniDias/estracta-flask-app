from sqlalchemy_serializer import SerializerMixin
from ..extensions.database import db


class Company(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cnpj = db.Column(db.BigInteger, unique=True, nullable=False)
    cnae = db.Column(db.Integer, nullable=False)
    nome_fantasia = db.Column(db.String(200), nullable=False)
    nome_razao = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=db.func.now())
    date_updated = db.Column(
        db.DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, nome_fantasia, nome_razao, cnpj, cnae):
        self.nome_fantasia = nome_fantasia
        self.nome_razao = nome_razao
        self.cnpj = cnpj
        self.cnae = cnae

    def __repr__(self):
        return f"{self.nome_razao} - {self.cnpj}" 
