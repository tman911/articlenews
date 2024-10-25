from django.apps import AppConfig



class UserappsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userapps'

    def ready(self):
        import userapps.signals
