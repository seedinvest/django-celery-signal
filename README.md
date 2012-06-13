django-celery-signal
====================

change:

from django import dispatch
project_cluster_event_details_changed_notification = dispatch.Signal(
    providing_args=["event", "project_cluster", "is_project", "is_cluster", "person"]
)

to 

from django_celery_signal.models import CeleryASyncSignal
project_cluster_event_details_changed_notification = CeleryASyncSignal(
    providing_args=["event", "project_cluster", "is_project", "is_cluster", "person"]
)
