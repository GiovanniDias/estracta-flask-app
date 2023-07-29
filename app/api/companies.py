from flask import Blueprint, Response


bp = Blueprint('companies', __name__, url_prefix="/api/v1/companies")


@bp.route('/', methods=['GET'])
def get_all_companies():
    status_code = 200
    return Response("Lista de empresas", status_code)


@bp.route('/', methods=['POST'])
def create_company():
    status_code = 201
    return Response("Empresa criada", status_code)


@bp.route('/<id>/', methods=['GET'])
def get_company(id):
    status_code = 200
    return Response("Empresa encontrada", status_code)


@bp.route('/<id>/', methods=['PUT', 'PATCH'])
def update_company(id):
    status_code = 200
    return Response("Empresa atualizada", status_code)


@bp.route('/<id>/', methods=['DELETE'])
def delete_company(id):
    status_code = 200
    return Response("Empresa removida", status_code)
