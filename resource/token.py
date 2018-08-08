import urllib3
from flask import request
from flask_restful import Resource

from resource.token_amil_service import get_justification, confirm_attendance
from utils.logger import logger

urllib3.disable_warnings()


class Amil(Resource):
    def get(self):
        try:
            return {"justification": get_justification()}, 200
        except Exception as e:
            logger.error("Error during get `Lista Justificativa Amil` %s", e)
            return {"message": "Error during send message {}!".format(e)}, 500

    def post(self):

        req = request.json
        try:

            logger.info("Confirmar atendimento - Ip %s, New request %s", request.remote_addr, req)

            result = confirm_attendance(req)

            logger.info("Confirmar atendimento - Ip %s, Response with success %s", request.remote_addr, result)

            return {
                       "message": "Success!",
                       "retorno": {
                           "codigo": result["Codigo"],
                           "mensagem": result["Mensagem"]
                       }
                   }, 200

        except Exception as e:

            logger.error("Ip %s, Error during send message %s", request.remote_addr, e)
            return {
                       "message": "Error during send message {}!".format(e)
                   }, 500
