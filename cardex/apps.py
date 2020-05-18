from django.apps import AppConfig


class CardexConfig(AppConfig):
    name = 'cardex'
    
    def ready(self):
        from . import signals
