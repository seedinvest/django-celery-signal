from celery.task import Task
from celery.registry import tasks


class SignalTask(Task):
    def run(self, receiver, sender, **named):
        logger = self.get_logger(**named)
        logger.debug("Running SignalTask for %s." % receiver)
        receiver(sender=sender, **named)
        return True

tasks.register(SignalTask)