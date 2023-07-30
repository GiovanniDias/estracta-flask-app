from flask import jsonify
from .repository import CompanyRepository


class CompanyController:
    @classmethod
    def get_all_companies(cls, params):
        # pagination_default
        START = 1
        LIMIT = 10
        SORT = "id"
        DIR = "asc"

        start = int(params.get("start", START))
        limit = int(params.get("limit", LIMIT))
        sort = params.get("sort", SORT)
        direction = params.get("dir", DIR)

        companies = CompanyRepository.list(start, limit, sort, direction)
        serialized = [company.to_dict() for company in companies]

        return jsonify(serialized)

    @classmethod
    def create_company(cls, data):
        nome_fantasia = data.get("nome_fantasia")
        nome_razao = data.get("nome_razao")
        cnpj = data.get("cnpj")
        cnae = data.get("cnae")

        company = CompanyRepository.create(
            nome_fantasia=nome_fantasia, nome_razao=nome_razao, cnpj=cnpj, cnae=cnae
        )
        serialized = company.to_dict()
        return jsonify(serialized)

    @classmethod
    def get_company(cls, id):
        company = CompanyRepository.get(id)
        serialized = company.to_dict()
        return jsonify(serialized)

    @classmethod
    def update_company(cls, id, data):
        cnae = data.get("cnae")
        nome_fantasia = data.get("nome_fantasia")

        company = CompanyRepository.update(id, cnae=cnae, nome_fantasia=nome_fantasia)
        serialized = company.to_dict()
        return jsonify(serialized)

    @classmethod
    def delete_company(cls, cnpj):
        CompanyRepository.delete(cnpj=cnpj)
