from flask import Blueprint, Response, make_response, request, abort, jsonify
from werkzeug.exceptions import NotFound
from .controller import CompanyController
from sqlalchemy.exc import NoResultFound


bp = Blueprint("company", __name__, url_prefix="/api/v1/company")

# LOGIN https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins


@bp.route("/", methods=["GET"])
def get_all_companies():
    try:
        params = request.args
        companies = CompanyController.get_all_companies(params)

        status_code = 200
        return make_response(companies, status_code)
    except AttributeError as error:
        return make_response(error, status_code=500)


@bp.route("/", methods=["POST"])
def create_company():
    try:
        data = request.get_json()
        company = CompanyController.create_company(data)

        status_code = 201
        return make_response(company, status_code)
    except ValueError as error:
        make_response(error, status_code=400)


@bp.route("/<id>/", methods=["GET"])
def get_company(id):
    try:
        company = CompanyController.get_company(id)
        status_code = 200
        return make_response(company, status_code)
    except Exception as error:  # TODO: check exception for 404
        make_response(error, status_code=404)


@bp.route("/<id>/", methods=["PUT", "PATCH"])
def update_company(id):
    try:
        data = request.get_json()
        company = CompanyController.update_company(id, data)

        status_code = 200
        return make_response(company, status_code)
    except ValueError as error:
        make_response(error, 400)
    except Exception as error:  # TODO: check exception for 404
        make_response(error, 404)


@bp.route("/<cnpj>/", methods=["DELETE"])
def delete_company(cnpj):
    try:
        CompanyController.delete_company(cnpj)
        status_code = 200
        return Response(status=status_code)
    except NoResultFound:
        status_code = 404
        return make_response(
            {"message": f"Nenhuma empresa encontrada com cnpj {cnpj}"},
            status_code
        )
