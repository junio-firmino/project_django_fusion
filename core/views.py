from django.views.generic import FormView
from .models import Funcionario, Servico, Cargo
from .forms import Contatoforms
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(FormView):
    template_name = "index.html"
    form_class = Contatoforms
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'E-mail não enviado.')
        return super(IndexView,self).form_invalid(form, *args, **kwargs)
