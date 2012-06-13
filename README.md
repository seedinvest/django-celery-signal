django-celery-signal
====================

change:

    from django import dispatch
    my_signal = dispatch.Signal(
        providing_args=["arg1", "arg2", "arg3"]
    )

to 

    from django_celery_signal.models import CeleryASyncSignal
    my_signal = CeleryASyncSignal(
        providing_args=["arg1", "arg2", "arg3"]
    )
