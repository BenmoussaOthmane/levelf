from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View ,TemplateView , ListView , DetailView , CreateView, UpdateView,DeleteView)
from . import models
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    

class ProduiteListView(ListView):
    context_object_name = 'Liste_pro' #hadi nsha9oha fal html liste bah yafichiholna 3al chakl liste 
    model = models.Produite
    template_name = 'Liste.html'
    

class ProduiteDetialView(DetailView):
    context_object_name = 'Detailpro'  # hadi stha9oha bah naffichou detail 
    model = models.Produite
    template_name = 'Detail.html'

class ProduiteCreateView(CreateView):
    fields = ('name' , 'qte' )  # hado les filed linstha9ohom bah ajoutou un neveau produi 3la hsab les atrubuer lirahom fal table produite
    model =  models.Produite
    template_name = 'CreateView.html'

class ProduiteUpdeat(UpdateView):
    fields = ('name' , 'qte')  #whadi bah ndir la modifications ta3  produite  
    model = models.Produite
    template_name = 'CreateView.html'

class ProduiteDelaite(DeleteView):
    model = models.Produite
    success_url = reverse_lazy("my_ap:produite")  # hadi  lazam ndiroha fal delete ndiroha tadi la ay page liste bah takhroj bali rahy  
    template_name = 'confirmdelete.html'