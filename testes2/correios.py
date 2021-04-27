import requests


class Correios(object):

    def __init__(self):
        self.__URL = 'http://api.postmon.com.br/v1/{}/{}'

    def _get_url(self, url, codigo):
        '''Retorna uma url para verificacao de cep ou encomenda.'''
        return self.__URL.format(url, codigo)

    def _request(self, url, codigo):
        try:
            data = requests.get(self._get_url(url, codigo)).json()
        except Exception as error:
            raise error
        return data

    def encomenda(self, codigo):
        data = self._request('rastreio/ect', codigo)
        return data

    def cep(self, cep):

        data = self._request('cep', cep)
        return data