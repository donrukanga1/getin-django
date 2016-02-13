from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView

from backend.models import PregnantGirl
from dashboard.forms import UpdateGirlForm


class GirlsList(LoginRequiredMixin, ListView):
    model = PregnantGirl
    paginate_by = 20
    template_name = 'dashboard/list.html'
    context_object_name = 'girls'


class GirlsMap(LoginRequiredMixin, ListView):
    model = PregnantGirl
    template_name = 'dashboard/map.html'
    context_object_name = 'girls'

class UpdateGirl(LoginRequiredMixin, UpdateView):
    model = PregnantGirl
    form_class = UpdateGirlForm
    template_name = 'dashboard/form.html'
    success_url = reverse_lazy('girls-list')
    context_object_name = 'girl'

class DeleteGirl(LoginRequiredMixin, DeleteView):
    model = PregnantGirl
    success_url = reverse_lazy('girls-list')
    template_name = 'dashboard/confirm_delete.html'
    context_object_name = 'girl'