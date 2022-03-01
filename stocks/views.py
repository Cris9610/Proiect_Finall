from django import forms
# from stocks.forms import Produsul
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from stocks.models import Pungi, Folie, Stocks


class produse_view(LoginRequiredMixin, CreateView):
    model = Stocks
    fields = '__all__'  # pe toate
    template_name = 'stocks/stocks.html'

    def get_success_url(self):
        return reverse('stocks:produse')


class pungi_view(LoginRequiredMixin, CreateView):
    model = Pungi
    fields = ['tip_punga',
              'inaltime_punga',
              'latime_punga',
              'inaltime_pliu',
              'grosime_folie_p',
              'zipper',
              'eurohole',
              'ciupitura',
              'cantitate']
    template_name = 'stocks/pungi.html'

    def get_success_url(self):
        return reverse('stocks:pungi')


class folie_view(LoginRequiredMixin, CreateView):
    model = Folie
    fields = ['tip_folie',
              'grosime_folie',
              'latime_folie',
              'cantitate']  # pe toate
    template_name = 'stocks/folie.html'

    def get_success_url(self):
        return reverse('stocks:folie')


class PungiView(LoginRequiredMixin, ListView):
    model = Pungi
    template_name = 'stocks/pungiview.html'
    paginate_by = 5

    def get_queryset(self):
        return Pungi.objects.filter(active=True)


class FolieView(LoginRequiredMixin, ListView):
    model = Folie
    template_name = 'stocks/folieview.html'
    paginate_by = 5

    def get_queryset(self):
        return Folie.objects.filter(active=True)


class UpdatePungiView(LoginRequiredMixin, UpdateView):
    model = Pungi
    fields = '__all__'
    template_name = 'stocks/pungi.html'

    def get_queryset(self):
        return Pungi.objects.filter(active=True)

    def get_success_url(self):
        return reverse('stocks:pungiview')


class UpdateFolieView(LoginRequiredMixin, UpdateView):
    model = Folie
    fields = '__all__'
    template_name = 'stocks/folie.html'

    def get_queryset(self):
        return Folie.objects.filter(active=True)

    def get_success_url(self):
        return reverse('stocks:folieview')


@login_required
def deactivate_Pungi(request, pk):
    if Pungi.objects.filter(id=pk).exists:
        Pungi.objects.filter(id=pk).update(active=False)
    return redirect('stocks:pungiview')


@login_required
def deactivate_Folie(request, pk):
    if Folie.objects.filter(id=pk).exists():
        Folie.objects.filter(id=pk).update(active=False)
    return redirect('stocks:folieview')


@login_required
def ComenziView(request):
    return render(request, 'comenzi.html')
