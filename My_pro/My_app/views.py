from django.shortcuts import render
from  django.views.generic import View , TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'html/index.html'

    def get_context_data(self , **kwargs):
        con = super().get_context_data(**kwargs)

        con['inj'] = ' injections'

        
        return  con 

