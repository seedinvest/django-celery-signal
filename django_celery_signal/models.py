from django.dispatch.dispatcher import Signal, _make_id
from django_celery_signal.tasks import SignalTask

class CeleryASyncSignal(Signal):
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

        for receiver in self._live_receivers(_make_id(sender)):
            SignalTask.delay(receiver=receiver, signal=self, sender=sender, **named)
#            response = receiver(signal=self, sender=sender, **named)

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
                SignalTask.delay(receiver=receiver, signal=self, sender=sender, **named)
#                receiver(signal=self, sender=sender, **named)
            except Exception, err:
                pass
