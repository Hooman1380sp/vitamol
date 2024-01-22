from django.apps import AppConfig
# from django.core.signals import request_finished

class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    verbose_name = 'ماژول وبلاگ ها'
    def ready(self):
        import blog.signals

