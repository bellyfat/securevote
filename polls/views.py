# from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Poll


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.filter(
                created_time__lte=timezone.now(),
                private=False
                ).order_by('-created_time')[:5]
