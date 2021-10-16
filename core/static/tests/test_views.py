from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class Indexviewtestcase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Junio firmino',
            'email': 'junio@gmail.com',
            'assunto': 'meu assunto pessoal',
            'mensagem': 'Minha mensagem'
        }

    def test_ford_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Junio firmino',
            'assunto': 'meu assunto particular',
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)
