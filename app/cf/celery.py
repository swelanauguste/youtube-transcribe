# # celery.py

# import os

# from celery import Celery

# # Set the default Django settings module
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cf.settings")

# # Create an instance of Celery
# app = Celery("cf")

# # Configure Celery
# app.config_from_object("django.conf:settings", namespace="CELERY")

# # Discover tasks in Django apps
# app.autodiscover_tasks()


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')