from zeep import Client
from flask import request
from flask_restful import Resource

URL = 'https://api.amil.com.br/sisamil-credenciado/prestador/conecta?wsdl'


class Amil(Resource):
    def post(self):
        try:
            req = request.json

            client = Client(URL)

            result = client.service.ConfirmarAtendimento(pedido=req["pedido"],
                                                         prestador=req["prestador"],
                                                         beneficiario=req["codMatriculaBeneficario"],
                                                         token=req["token"] if 'token' in req and req[
                                                             "token"] else None,
                                                         dataAtendimento=req["dataAtendimento"],
                                                         horaAtendimento=req["horaAtendimento"],
                                                         justificativaConfirmacaoSemToken=req["retorno"])

            return {"message": "Success!",
                    "retorno": {"codigo": result["Codigo"], "mensagem": result["Mensagem"]}}, 200

        except Exception as e:
            return {"message": "Error during send message {}!".format(e)}, 500
