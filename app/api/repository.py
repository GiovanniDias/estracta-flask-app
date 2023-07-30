from sqlalchemy.exc import NoResultFound
from werkzeug.exceptions import NotFound
from ..extensions.database import db
from ..models.company import Company


class CompanyRepository:
    @classmethod
    def list(cls, start, limit, sort, direction):
        results = (
            Company.query.order_by(getattr(getattr(Company, sort), direction)())
            .paginate(page=start, per_page=limit, error_out=False)
            .items
        )
        return results

    @classmethod
    def create(cls, nome_fantasia, nome_razao, cnpj, cnae):
        instance = Company(
            nome_fantasia=nome_fantasia, nome_razao=nome_razao, cnpj=cnpj, cnae=cnae
        )
        db.session.add(instance)
        db.session.commit()
        return instance

    @classmethod
    def get(cls, id):
        instance = Company.query.get_or_404(id)
        return instance

    @classmethod
    def update(cls, id, cnae=None, nome_fantasia=None):
        instance = Company.query.get_or_404(id)

        if cnae is not None:
            instance.cnae = cnae
        if nome_fantasia is not None:
            instance.nome_fantasia = nome_fantasia

        db.session.add(instance)
        db.session.commit()

        return instance

    @classmethod
    def delete(cls, cnpj):
        instance = Company.query.filter_by(cnpj=cnpj).one()
        db.session.delete(instance)
        db.session.commit()
