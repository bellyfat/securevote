from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        return context
