from django.dispatch.dispatcher import Signal, _make_id
from django_celery_signal.tasks import SignalTask

class CeleryASyncSignal(Signal):

    def __init__(self, task_queue=None, task_priority=None, *args, **kwargs):
        self.task_queue = task_queue
        self.task_priority = task_priority
        super(CeleryASyncSignal, self).__init__(args, kwargs)

    def send(self, sender, **named):
        """
        Send signal from sender to all connected receivers.

        If any receiver raises an error, the error propagates back through send,
        terminating the dispatch loop, so it is quite possible to not have all
        receivers called if a raises an error.

        Arguments:

            sender
                The sender of the signal Either a specific object or None.

            named
                Named arguments which will be passed to receivers.

        Return nothing
        """
        if not self.receivers:
            return

        task_args = {}
        if 'task_args' in named:
           task_args = named.pop('task_args')

        for receiver in self._live_receivers(_make_id(sender)):
            kwargs = {"receiver": receiver, "sender": sender }
            kwargs.update(named)

            SignalTask.apply_async(kwargs=kwargs, queue=self.task_queue, priority=self.task_priority, **task_args)

    def send_robust(self, sender, **named):
        """
        Send signal from sender to all connected receivers catching errors.

        Arguments:

            sender
                The sender of the signal. Can be any python object (normally one
                registered with a connect if you actually want something to
                occur).

            named
                Named arguments which will be passed to receivers. These
                arguments must be a subset of the argument names defined in
                providing_args.

        Return nothing

        """
        if not self.receivers:
            return

        # Call each receiver with whatever arguments it can accept.
        # Return a list of tuple pairs [(receiver, response), ... ].
        for receiver in self._live_receivers(_make_id(sender)):
            try:
                SignalTask.delay(receiver=receiver, sender=sender, **named)
            except Exception, err:
                pass
