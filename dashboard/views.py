from braces.views import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView

from backend.models import PregnantGirl


class GirlsList(LoginRequiredMixin, ListView):
    model = PregnantGirl
    template_name = 'dashboard/list.html'
    context_object_name = 'girls'


class GirlsMap(LoginRequiredMixin, ListView):
    model = PregnantGirl
    template_name = 'dashboard/map.html'
    context_object_name = 'girls'

class UpdateGirl(LoginRequiredMixin, UpdateView):
    model = PregnantGirl
    template_name = 'dashboard/update.html'
    context_object_name = 'girl'

class DeleteGirl(LoginRequiredMixin, DeleteView):
    model = PregnantGirl
    template_name = 'dashboard/update.html'
    context_object_name = 'girl'