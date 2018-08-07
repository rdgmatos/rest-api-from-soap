import urllib3
from utils.logger import logger
from zeep import Client
from flask import request
from flask_restful import Resource

urllib3.disable_warnings()

URL = 'https://api.amil.com.br/sisamil-credenciado/prestador/conecta?wsdl'


class Amil(Resource):
    def post(self):

        req = request.json
        try:

            logger.info("Confirmar atendimento - Ip %s, New request %s", request.remote_addr, req)
            client = Client(URL)

            result = client.service.ConfirmarAtendimento(pedido=req["pedido"],
                                                         prestador=req["prestador"],
                                                         beneficiario=req["codMatriculaBeneficario"],
                                                         token=req["token"] if 'token' in req and req[
                                                             "token"] else None,
                                                         dataAtendimento=req["dataAtendimento"],
                                                         horaAtendimento=req["horaAtendimento"],
                                                         justificativaConfirmacaoSemToken=req["retorno"])

            logger.info("Confirmar atendimento - Ip %s, Response with success %s", request.remote_addr, result)

            return {
                       "message": "Success!",
                       "retorno": {
                           "codigo": result["Codigo"],
                           "mensagem": result["Mensagem"]
                       }
                   }, 200

        except Exception as e:

            logger.error("Confirmar atendimento - Ip %s, Error during send message %s", request.remote_addr, e)
            return {
                       "message": "Error during send message {}!".format(e)
                   }, 500
