from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class PollsConfig(ModuleMixin, AppConfig):
    name = 'polls'
    icon = '<i class="mdi-communication-quick-contacts-dialer"></i>'
