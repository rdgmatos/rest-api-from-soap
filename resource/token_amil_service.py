import os

from zeep import Client

from utils.cache import cache

CLIENT_WSDL = Client(os.environ.get("URL_AMIL", "https://api.amil.com.br/sisamil-credenciado/prestador/conecta?wsdl"))


@cache.cached(timeout=50)
def get_justification():
    response_amil = []
    response = CLIENT_WSDL.service.BuscarJustificativaConfirmacaoSemToken()
    for r in response:
        response_amil.append({'codigo': r["Codigo"], 'message': r['Mensagem']})

    return response_amil


def confirm_attendance(data):
    return CLIENT_WSDL.service.ConfirmarAtendimento(pedido=data["pedido"],
                                                    prestador=data["prestador"],
                                                    beneficiario=data["codMatriculaBeneficario"],
                                                    token=data["token"] if 'token' in data and data[
                                                        "token"] else None,
                                                    dataAtendimento=data["dataAtendimento"],
                                                    horaAtendimento=data["horaAtendimento"],
                                                    justificativaConfirmacaoSemToken=data["retorno"])
