from django.test import TestCase
from core.forms import Contatoforms


class Contatoformtestcase(TestCase):

    def setUp(self):
        self.nome = 'Junio Firmino'
        self.email = 'junio@gmail.com'
        self.assunto = 'um assunto'
        self.mensagem = 'Outra mensagem'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }

        self.form = Contatoforms(data=self.dados)

    def test_send_mail(self):
        form1 = Contatoforms(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)
