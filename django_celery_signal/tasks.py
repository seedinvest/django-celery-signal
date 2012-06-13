from celery.task import Task
from celery.registry import tasks


class SignalTask(Task):
    def run(self, receiver, signal, sender, **named):
        logger = self.get_logger(**kwargs)
        logger.debug("Running SignalTask for %s." % receiver)
        receiver(signal=signal, sender=sender, **named)
        return True

tasks.register(SignalTask)